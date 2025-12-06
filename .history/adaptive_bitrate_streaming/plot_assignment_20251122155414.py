import pandas as pd
import matplotlib.pyplot as plt
import glob
import os

# 1. Find the latest results CSV file
# The code looks recursively in artifacts/results for any .csv file
search_path = 'artifacts/results/**/*.csv'
files = glob.glob(search_path, recursive=True)

if not files:
    print("Error: No result files found! Make sure the test command finished.")
else:
    # Get the newest file (the one you just generated)
    latest_file = max(files, key=os.path.getctime)
    print(f"Plotting data from: {latest_file}")

    # 2. Read the data
    df = pd.read_csv(latest_file)

    # 3. Plot the Reward Curve
    plt.figure(figsize=(10, 6))
    # Plotting first 100 chunks to make the graph readable
    plt.plot(df['reward'][:100], label='NetLLM Reward (1 Epoch)',
             color='blue', linewidth=1.5)

    plt.title('NetLLM Performance: Reward vs Time', fontsize=14)
    plt.xlabel('Video Chunks (Time Steps)', fontsize=12)
    plt.ylabel('Reward (QoE)', fontsize=12)
    plt.legend()
    plt.grid(True, linestyle='--', alpha=0.6)

    # 4. Save the image
    output_filename = 'final_graph_for_report.png'
    plt.savefig(output_filename)
    print(f"Success! Graph saved as '{output_filename}'")
