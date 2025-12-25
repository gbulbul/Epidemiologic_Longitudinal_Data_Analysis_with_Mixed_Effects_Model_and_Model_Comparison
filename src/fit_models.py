import pandas as pd
import statsmodels.formula.api as smf
import statsmodels.api as sm


def fit_lmm_full(df):
    """
    Full linear mixed-effects model
    """
    model = smf.mixedlm(
        "outcome ~ treatment + time + age + biomarker",
        df,
        groups=df["id"]
    )
    return model.fit(reml=False)


def fit_lmm_reduced(df):
    """
    Reduced mixed model (fewer covariates)
    """
    model = smf.mixedlm(
        "outcome ~ treatment + time",
        df,
        groups=df["id"]
    )
    return model.fit(reml=False)




def fit_gee_exchangeable(df):
    """
     GEE with exchangeable working correlation
     Valid for QIC-based model comparison
    """
    model = smf.gee(
        "outcome ~ treatment + time + age + biomarker",
        groups="id",
        data=df,
        family=sm.families.Gaussian(),
        cov_struct=sm.cov_struct.Exchangeable()
    )

    result = model.fit()

    scale = result.pearson_chi2 / result.df_resid

    # 🔴 CRITICAL FIX (THIS IS WHAT WAS MISSING)
    result.scale = scale
    result.model.scale = scale

    return result

def fit_gee_independence(df):
    """
    GEE with independence working correlation
    Valid for QIC-based comparison
    """
    model = smf.gee(
        "outcome ~ treatment + time + age + biomarker",
        groups="id",
        data=df,
        family=sm.families.Gaussian(),
        cov_struct=sm.cov_struct.Independence()
    )

    result = model.fit()

    scale = result.pearson_chi2 / result.df_resid
    result.scale = scale
    result.model.scale = scale

    return result

