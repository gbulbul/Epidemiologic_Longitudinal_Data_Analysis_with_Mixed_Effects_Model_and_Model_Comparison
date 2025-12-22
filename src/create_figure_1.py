mport matplotlib.pyplot as plt
import seaborn as sns

# Model comparison results
models = ["Linear Mixed Model", "Random Forest", "X-Learner"]
aic_scores = [320.5, 310.2, 305.8]

# Style (academic look)
sns.set(style="whitegrid", context="talk")

plt.figure(figsize=(8, 5))

bars = plt.bar(
    models,
    aic_scores,
    color=["#4C72B0", "#55A868", "#C44E52"]
)

# Annotate bars with values
for bar in bars:
    height = bar.get_height()
    plt.text(
        bar.get_x() + bar.get_width() / 2,
        height - 3,
        f"{height:.1f}",
        ha="center",
        va="top",
        color="white",
        fontsize=11,
        fontweight="bold"
    )

plt.ylabel("AIC Score (lower is better)")
plt.title("Model Comparison Based on AIC", pad=15)
plt.tight_layout()

# Save figure
plt.savefig("figures/figure_1_model_comparison.png", dpi=300)
plt.show()
