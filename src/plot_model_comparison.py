import matplotlib.pyplot as plt

# Example model comparison results
models = ["Linear Mixed Model", "Random Forest", "X-Learner"]
aic_scores = [320.5, 310.2, 305.8]

plt.figure(figsize=(8, 5))
plt.bar(models, aic_scores)
plt.ylabel("AIC Score")
plt.title("Model Comparison Based on AIC")
plt.xticks(rotation=20)
plt.tight_layout()

# SAVE FIGURE
plt.savefig("figures/figure_1_model_comparison.png", dpi=300)

plt.show()
