import pandas as pd
import numpy as np
from fit_models import (
    fit_lmm_full,
    fit_lmm_reduced,
    fit_gee_exchangeable,
    fit_gee_independence
)
from simulate_longitudinal import simulate_longitudinal_data

def rmse(y, yhat):
    return np.sqrt(np.mean((y - yhat) ** 2))


if __name__ == "__main__":

    # Simulate data
    df = simulate_longitudinal_data()

    # Fit models
    lmm_full = fit_lmm_full(df)
    lmm_reduced = fit_lmm_reduced(df)
    gee_ex = fit_gee_exchangeable(df)
    gee_ind = fit_gee_independence(df)

    print("\n--- MIXED MODELS ---")
    print("Full LMM  | AIC:", lmm_full.aic, "BIC:", lmm_full.bic)
    print("Reduced LMM | AIC:", lmm_reduced.aic, "BIC:", lmm_reduced.bic)

    lr_stat = 2 * (lmm_full.llf - lmm_reduced.llf)
    df_diff = lmm_full.df_modelwc - lmm_reduced.df_modelwc
    print("Likelihood Ratio Test:", lr_stat, "df:", df_diff)

    print("\n--- GEE MODELS ---")
    print("GEE Exchangeable QIC:", gee_ex.qic())
    print("GEE Independence  QIC:", gee_ind.qic())

    # Prediction error (LMM)
    df["pred_lmm"] = lmm_full.predict(df)
    print("\nLMM RMSE:", rmse(df["outcome"], df["pred_lmm"]))

