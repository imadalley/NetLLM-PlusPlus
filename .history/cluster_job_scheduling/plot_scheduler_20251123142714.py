import matplotlib.pyplot as plt

# YOUR RESULTS
baseline = 66.125
improved = 63.140

labels = ['Baseline (Rank 8)', 'Improved (Rank 128)']
values = [baseline, improved]
colors = ['grey', '#28CD41']  # Grey, Green

plt.figure(figsize=(8, 6))
bars = plt.bar(labels, values, color=colors, width=0.6)

# Add numbers on top
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval, 2),
             ha='center', va='bottom', fontweight='bold')

plt.title('Cluster Job Scheduling Improvement', fontsize=14)
plt.ylabel('Avg Job Duration (Seconds) - Lower is Better', fontsize=12)
plt.ylim(50, 70)  # Zoom in to show difference clearly
plt.grid(axis='y', linestyle='--', alpha=0.5)

plt.savefig('scheduler_improvement.png')
print("Graph saved as 'scheduler_improvement.png'")
