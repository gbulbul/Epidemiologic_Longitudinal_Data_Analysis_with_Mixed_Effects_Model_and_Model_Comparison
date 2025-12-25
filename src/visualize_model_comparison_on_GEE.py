import matplotlib.pyplot as plt

models = ["GEE Exchangeable", "GEE Independence"]
qic_values = [1012.58, 1008.72]

plt.figure(figsize=(6, 4))
plt.bar(models, qic_values)
plt.ylabel("QIC")
plt.title("GEE Model Comparison (QIC)")
plt.tight_layout()
plt.show()
