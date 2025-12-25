# epi_longitudinal

Applied longitudinal epidemiology project on simulated data with model comparison.

## Models
- Linear Mixed-Effects Models (full vs reduced)
- GEE with different working correlation structures

## Model Selection
- AIC / BIC (Mixed Models)
- Likelihood Ratio Test (nested models)
- QIC (GEE)
- Prediction error (RMSE)

## Goal
Demonstrate model selection procedure for longitudinal epidemiologic data.

## Project Structure

- `src/`: Python scripts for model fitting and visualization  
- `sql/`: SQL scripts for longitudinal data preparation

Results:

### Model Comparison: Linear Mixed-Effects Models

| Metric | Full LMM | Reduced LMM |
|------|---------:|------------:|
| AIC | 3187.33 | 3426.75 |
| BIC | 3221.68 | 3451.29 |

*Lower AIC and BIC indicate better model fit.*
**INTERPRETATION**
Full LMM clearly outperforms the reduced model. The additional predictors in the full model are important for explaining the outcome.

**### Likelihood Ratio Test (LRT)**
LR statistic = 243.42, df = 2 (Very large LR statistic with small df)
**INTERPRETATION**
This strongly indicates that the full model provides a significantly better fit. This suggests the excluded terms in the reduced model have a statistically meaningful effect on the outcome. The outcome is strongly influenced by the predictors included in the full mixed-effects model.

**### Model Comparison: GEE Models (Population-Averaged)**

| Metric | GEE Exchangeable | GEE Independence |
|------|----------------:|----------------:|
| QIC |      1012.58     | 1008.72 |

*Lower QIC indicates better fit among GEE models.*

GEE Independence has a lower QIC (1008.72 vs 1012.58). This indicates that:
Modeling within-subject correlation does not substantially improve fit. Thus, within-subject correlation is weak or negligible in this dataset.

Two GEE models are with the same mean structure.Difference lies only in the working correlation structure:

**Exchangeable**: constant correlation among repeated measures, **Independence**: assumes no within-subject correlation

**INTERPRETATION**
Among GEE models, the independence working correlation provided a slightly better fit than the exchangeable structure, suggesting minimal impact of within-subject correlation on the population-averaged mean outcome.

**###Prediction Performance (LMM)**
RMSE = 1.28
**INTERPRETATION**
On average, predictions deviate from observed outcomes by ~1.28 units. Indicates reasonable predictive accuracy for longitudinal data.

**NOTE**: RMSE is used only for LMM, not for GEE (GEE is not predictive)











