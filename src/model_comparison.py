import pandas as pd
import numpy as np
import warnings

from simulate_longitudinal import simulate_longitudinal_data
from fit_models import (
    fit_lmm_full,
    fit_lmm_reduced,
    fit_gee_exchangeable,
    fit_gee_independence
)

# ---------------------------
# Utility
# ---------------------------
def rmse(y, yhat):
    return np.sqrt(np.mean((y - yhat) ** 2))


# ---------------------------
# Main
# ---------------------------
if __name__ == "__main__":

    # 1) Simulate data
    df = simulate_longitudinal_data()

    # 2) Fit models
    lmm_full = fit_lmm_full(df)
    lmm_reduced = fit_lmm_reduced(df)

    gee_ex = fit_gee_exchangeable(df)
    gee_ind = fit_gee_independence(df)

    # ---------------------------
    # LMM comparison
    # ---------------------------
    print("\n--- LINEAR MIXED MODELS ---")
    print("Full LMM    | AIC:", lmm_full.aic, "BIC:", lmm_full.bic)
    print("Reduced LMM | AIC:", lmm_reduced.aic, "BIC:", lmm_reduced.bic)

    lr_stat = 2 * (lmm_full.llf - lmm_reduced.llf)
    df_diff = lmm_full.df_modelwc - lmm_reduced.df_modelwc

    print("Likelihood Ratio Test:")
    print("  LR statistic:", lr_stat)
    print("  df:", df_diff)

    # ---------------------------
    # GEE comparison (QIC)
    # ---------------------------
    print("\n--- GEE MODELS ---")

    # WARNING ONLY SUPPRESSED HERE (CORRECT PLACE)
    with warnings.catch_warnings():
        warnings.filterwarnings(
            "ignore",
            message="QIC values obtained using scale=None"
        )
        qic_ex = gee_ex.qic()
        qic_ind = gee_ind.qic()

    print("GEE Exchangeable | QIC:", qic_ex)
    print("GEE Independence | QIC:", qic_ind)

    # ---------------------------
    # Prediction error (LMM only)
    # ---------------------------
    df["pred_lmm"] = lmm_full.predict(df)
    print("\nLMM RMSE:", rmse(df["outcome"], df["pred_lmm"]))
<<<<<<< HEAD
=======


>>>>>>> d47c792b5354368553749af1e5bedcddb503c5fa
