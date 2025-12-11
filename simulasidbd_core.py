# simulasidbd_core.py — FINAL VERSION (Compatible with app.py Glassmorphism)
import pandas as pd
import numpy as np
from scipy.integrate import odeint
from scipy.optimize import curve_fit

# ============================================================
# LOAD & PREPARE DATA
# ============================================================
def load_and_prep(csv_path, manual_date_col=None, manual_case_col=None):
    df = pd.read_csv(csv_path)

    # Manual column selection
    if manual_date_col is not None:
        date_col = manual_date_col
        case_col = manual_case_col
    else:
        # Auto-detect date column
        probable = []
        for c in df.columns:
            try: pd.to_datetime(df[c])
            except: continue
            probable.append(c)

        if len(probable) == 0:
            raise ValueError("Tidak ditemukan kolom tanggal!")
        date_col = probable[0]

        # Auto-detect numeric column
        nums = df.select_dtypes(include=["int","float"]).columns
        if len(nums) == 0:
            raise ValueError("Tidak ditemukan kolom kasus numerik!")
        case_col = nums[-1]

    df[date_col] = pd.to_datetime(df[date_col])
    df = df.dropna(subset=[date_col])
    df = df.sort_values(date_col).reset_index(drop=True)

    t = np.arange(len(df))
    I = df[case_col].astype(float).values

    return df, t, I, date_col, case_col

# ============================================================
# SIR MODEL
# ============================================================
def sir_ode(y, t, β, γ):
    S, I, R = y
    dS = -β * S * I
    dI = β * S * I - γ * I
    dR = γ * I
    return [dS, dI, dR]

def fit_sir(t, I_data):
    I0 = I_data[0]
    S0 = 1 - I0
    R0 = 0
    y0 = [S0, I0, R0]

    def sir_curve(t, β, γ):
        sol = odeint(sir_ode, y0, t, args=(β,γ))
        return sol[:,1]

    try:
        popt, pcov = curve_fit(sir_curve, t, I_data, bounds=(0,10))
        β, γ = popt
    except:
        β, γ = 0.3, 0.1

    sol = odeint(sir_ode, y0, t, args=(β,γ))
    I_pred = sol[:,1]
    rmse = np.sqrt(np.mean((I_pred - I_data)**2))

    return {
        "sol": sol,
        "rmse": rmse,
        "params": (β, γ)
    }

# ============================================================
# ROSS–MACDONALD MODEL
# ============================================================
def rm_ode(y, t, a, b, c, μv):
    Sh, Ih, Rh, Sv, Iv = y
    dSh = -a*b*Sh*Iv
    dIh = a*b*Sh*Iv - 0.1*Ih
    dRh = 0.1*Ih
    dSv = -a*c*Sv*Ih - μv*Sv
    dIv = a*c*Sv*Ih - μv*Iv
    return [dSh, dIh, dRh, dSv, dIv]

def fit_rm(t, I_data, N_h, N_v, Iv0):
    Sh0 = N_h - I_data[0]
    Ih0 = I_data[0]
    Rh0 = 0
    Sv0 = N_v - Iv0
    Iv0 = Iv0
    y0 = [Sh0, Ih0, Rh0, Sv0, Iv0]

    def rm_curve(t, a, b, c, μv):
        sol = odeint(rm_ode, y0, t, args=(a,b,c,μv))
        return sol[:,1]  # Ih

    try:
        popt, pcov = curve_fit(rm_curve, t, I_data, bounds=(0,2))
        a, b, c, μv = popt
    except:
        a, b, c, μv = 0.2, 0.3, 0.3, 0.1

    sol = odeint(rm_ode, y0, t, args=(a,b,c,μv))
    Ih_pred = sol[:,1]
    rmse = np.sqrt(np.mean((Ih_pred - I_data)**2))

    return {
        "sol": sol,
        "rmse": rmse,
        "params": (a, b, c, μv)
    }

# ============================================================
# MAIN PIPELINE
# ============================================================
def run_pipeline(csv_path, use_sir=True, use_rm=True,
                 N_h=1e6, N_v=1e6, Iv0=1000,
                 manual_date_col=None,
                 manual_case_col=None):

    df, t, I, dc, cc = load_and_prep(
        csv_path,
        manual_date_col,
        manual_case_col
    )

    results = {
        "df": df,
        "t": t,
        "I": I,
        "date_col": dc,
        "case_col": cc
    }

    if use_sir:
        results["sir"] = fit_sir(t, I)

    if use_rm:
        results["rm"] = fit_rm(t, I, N_h, N_v, Iv0)

    return results
