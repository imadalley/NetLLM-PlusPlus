import matplotlib.pyplot as plt

# 1. Exact path to the file you just verified
file_path = "artifacts/results/fcc-test_video1/trace_num_100_fixed_True/gpt2_base/early_stop_-1_rank_-1_w_20_gamma_1.0_tgt_scale_1.0_seed_100003/result_sim_abr_fcc-test_000_trace_942154_http---www.ebay.com_0"

rewards = []
bitrates = []

print(f"Reading file: {file_path}")

# 2. Read the data
try:
    with open(file_path, 'r') as f:
        for line in f:
            parts = line.strip().split()
            if len(parts) >= 8:
                # The last column (index -1) is the Reward
                rewards.append(float(parts[-1]))
                # The second column (index 1) is the Bitrate (e.g., 300, 2850)
                # Convert to Mbps for easier reading
                bitrates.append(float(parts[1]) / 1000.0)

    # 3. Generate the Graph
    plt.figure(figsize=(10, 6))

    # Plot Reward
    plt.plot(rewards, label='Reward (QoE)', color='#007AFF',
             linewidth=2, marker='o', markersize=4)

    # Add titles and labels
    plt.title('NetLLM Performance: Reward per Video Chunk', fontsize=14)
    plt.xlabel('Video Chunk Index', fontsize=12)
    plt.ylabel('Reward', fontsize=12)
    plt.grid(True, linestyle='--', alpha=0.6)
    plt.legend()

    # 4. Save the image
    output_file = "netllm_final_graph.png"
    plt.savefig(output_file)
    print(f"\nSUCCESS! Graph saved as: {output_file}")

except FileNotFoundError:
    print("Error: File not found. Please check the path again.")
except Exception as e:
    print(f"An error occurred: {e}")
