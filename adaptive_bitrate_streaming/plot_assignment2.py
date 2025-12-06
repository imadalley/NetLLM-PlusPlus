import matplotlib.pyplot as plt

# YOUR EXACT RESULTS
baseline = -40.55
imp1 = -37.84
imp2 = -37.96

results = [baseline, imp1, imp2]
labels = ['Baseline\n(Default)', 'Imp 1\n(Rank 32)',
          'Imp 2\n(Rank 32 + Win 40)']
colors = ['#95a5a6', '#2ecc71', '#3498db']  # Grey, Green (Best), Blue

plt.figure(figsize=(10, 6))
bars = plt.bar(labels, results, color=colors, edgecolor='black', alpha=0.9)

# Add numbers on top
for bar in bars:
    yval = bar.get_height()
    plt.text(bar.get_x() + bar.get_width()/2, yval + 0.5, round(yval, 2),
             ha='center', va='bottom', fontweight='bold', fontsize=12)

plt.title('Assignment 2: NetLLM Improvements (Adaptive Bitrate)', fontsize=14)
plt.ylabel('Mean Reward (QoE) - Higher is Better', fontsize=12)
plt.grid(axis='y', linestyle='--', alpha=0.5)
plt.axhline(0, color='black', linewidth=0.8)

plt.savefig('assignment2_final_graph.png')
print("Success! Graph saved as 'assignment2_final_graph.png'")
