import matplotlib.pyplot as plt
import numpy as np

# Model names
models = [
    "Random Intercept LMM",
    "Random Slope LMM",
    "GEE"
]

# Example model comparison metrics
aic = [1203.4, 1187.2, 1215.9]
bic = [1235.1, 1225.6, 1242.3]
rmse = [2.31, 2.05, 2.42]

# Create figures folder if it does not exist
import os
os.makedirs("figures", exist_ok=True)

# ---- AIC / BIC plot ----
x = np.arange(len(models))
width = 0.35

plt.figure(figsize=(8, 5))
plt.bar(x - width/2, aic, width, label="AIC")
plt.bar(x + width/2, bic, width, label="BIC")
plt.xticks(x, models, rotation=20)
plt.ylabel("Information Criterion")
plt.title("Model Comparison Using AIC and BIC")
plt.legend()
plt.tight_layout()
plt.savefig("figures/aic_bic_comparison.png", dpi=300)
plt.close()

# ---- RMSE plot ----
plt.figure(figsize=(7, 4))
plt.bar(models, rmse, color="darkorange")
plt.ylabel("RMSE")
plt.title("Predictive Performance Comparison")
plt.tight_layout()
plt.savefig("figures/rmse_comparison.png", dpi=300)
plt.close()
