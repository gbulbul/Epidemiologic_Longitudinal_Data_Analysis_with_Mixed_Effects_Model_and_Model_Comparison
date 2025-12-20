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
    GEE with exchangeable correlation
    """
    model = smf.gee(
        "outcome ~ treatment + time + age + biomarker",
        groups="id",
        data=df,
        cov_struct=sm.cov_struct.Exchangeable()
    )
    return model.fit()


def fit_gee_independence(df):
    """
    GEE with independence correlation
    """
    model = smf.gee(
        "outcome ~ treatment + time + age + biomarker",
        groups="id",
        data=df,
        cov_struct=sm.cov_struct.Independence()
    )
    return model.fit()

