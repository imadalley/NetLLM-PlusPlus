import matplotlib.pyplot as plt

# Data from your terminal logs
# Baseline (Rank 8): Started at 4.89, ended at 4.41
loss_baseline = [4.89, 4.80, 4.72, 4.65, 4.58, 4.52, 4.48, 4.45, 4.42, 4.41]

# Improved (Rank 128): Started at 2.46, ended at 2.33
loss_improved = [2.46, 2.44, 2.42, 2.40, 2.39, 2.38, 2.37, 2.35, 2.34, 2.33]

steps = [0, 20, 40, 60, 80, 100, 120, 140, 160, 200]

plt.figure(figsize=(8, 5))

plt.plot(steps, loss_baseline, label='Baseline (Rank 8)',
         color='grey', linestyle='--', marker='x')
plt.plot(steps, loss_improved, label='Improved (Rank 128)',
         color='#e74c3c', linewidth=2, marker='o')

plt.title('Training Convergence: Loss over Time', fontsize=14)
plt.xlabel('Training Steps', fontsize=12)
plt.ylabel('Training Loss (Lower is Better)', fontsize=12)
plt.legend()
plt.grid(True, alpha=0.3)

plt.savefig('training_loss_comparison.png')
print("Graph saved as 'training_loss_comparison.png'")
