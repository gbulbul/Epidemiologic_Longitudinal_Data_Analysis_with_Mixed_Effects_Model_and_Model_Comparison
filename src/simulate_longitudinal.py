import numpy as np
import pandas as pd

def simulate_longitudinal_data(
    n_subjects=200,
    n_timepoints=5,
    seed=42
):
    """
    Simulate longitudinal epidemiological data with
    time-varying covariates and outcomes.
    """
    np.random.seed(seed)

    data = []

    for i in range(n_subjects):
        baseline_age = np.random.normal(50, 10)
        treatment = np.random.binomial(1, 0.5)
        random_intercept = np.random.normal(0, 1)

        for t in range(n_timepoints):
            time = t
            biomarker = (
                0.3 * time
                + 0.5 * treatment
                + random_intercept
                + np.random.normal(0, 1)
            )

            outcome = (
                0.2 * time
                + 1.0 * treatment
                + 0.4 * biomarker
                + random_intercept
                + np.random.normal(0, 1)
            )

            data.append({
                "id": i,
                "time": time,
                "age": baseline_age,
                "treatment": treatment,
                "biomarker": biomarker,
                "outcome": outcome
            })

    return pd.DataFrame(data)


if __name__ == "__main__":
    df = simulate_longitudinal_data()
    print(df.head())


