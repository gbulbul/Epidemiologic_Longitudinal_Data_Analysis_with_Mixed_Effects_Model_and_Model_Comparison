import matplotlib.pyplot as plt
import pandas as pd

# Model comparison table
df_lmm = pd.DataFrame({
    "Model": ["Full LMM", "Reduced LMM"],
    "AIC": [3187.33, 3426.75],
    "BIC": [3221.68, 3451.29]
})

df_lmm = df_lmm.set_index("Model")

# Plot
ax = df_lmm.plot(kind="bar", figsize=(7, 4))
ax.set_ylabel("Information Criterion Value")
ax.set_title("LMM Model Comparison (AIC & BIC)")
plt.xticks(rotation=0)
plt.tight_layout()
plt.show()
