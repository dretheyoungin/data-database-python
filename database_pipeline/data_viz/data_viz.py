import matplotlib.pyplot as plt

print("Bot: Initializing Matplotlib Chart Generation Pipeline...")

# Simulated accuracy metrics for your completed portfolio models
models = [
    "Rule-Based\nClassifier",
    "Basic ML\nClassifier",
    "Enterprise\nModel"
]
accuracy_scores = [75, 88, 94] # Percentage scores out of 100

print("Bot: Compiling numerical data matrices into canvas layers...")

# Create a clean bar chart layout
plt.figure(figsize=(8, 5))
plt.bar(models, accuracy_scores, color=["#3498db", "#2ecc71", "#9b59b6"])

# Design labels and scale constraints
plt.title("AI Portfolio Model Performance Comparison", fontsize=14, fontweight="bold")
plt.xlabel("Engine Model Architecture", fontsize=12)
plt.ylabel("Accuracy Performance (%)", fontsize=12)
plt.ylim(0, 100) # Force scale to start at 0 and go to 100

print("Bot: Rendering visual plot grid...")
# Automatically save the graph image directly inside your portfolio folder!
plt.savefig("model_performance.png", dpi=300, bbox_inches="tight")
print("Bot: Success! Chart generated and exported as 'model_performance.png'.")