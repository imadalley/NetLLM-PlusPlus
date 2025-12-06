# NetLLM++: Resource-Efficient Fine-Tuning of Small LLMs for Edge Networking

This repository contains the source code and reproduction scripts for **NetLLM++**, an optimized framework designed to deploy Large Language Models (LLMs) for network control on resource-constrained edge devices.

This project reproduces the [ACM SIGCOMM 2024 NetLLM framework](https://dl.acm.org/doi/10.1145/3651890.3672268) using **GPT-2 Base** on consumer-grade CPUs (Intel MacBook Pro) and introduces **High-Rank LoRA** optimizations to improve performance.

---

## 👥 Authors (Group G-12)

- **Imad Ali** - [ibangash.msit25seecs@seecs.edu.pk](mailto:ibangash.msit25seecs@seecs.edu.pk)
- **Bilal Raza**
- **Fawad Khan**
- **Supervisor:** Prof. Dr. Muhammad Khuram Shahzad  
   _(School of Electrical Engineering & Computer Science, NUST, Islamabad)_

---

## 🚀 Project Overview

Standard LLM adaptations for networking often require server-grade GPUs (A100s) and suffer from underfitting due to conservative fine-tuning strategies. **NetLLM++** addresses these gaps by:

1.  **Enabling Edge Deployment:** We successfully ported the training pipeline to run on **Intel Core i5 CPUs** (MacBook Pro), resolving legacy dependency conflicts in `tflearn` and `gymnasium`.
2.  **Optimizing Model Capacity:** We demonstrated that standard LoRA settings ($r=8$) are insufficient for networking. By increasing the rank to **$r=32$ (Streaming)** and **$r=128$ (Scheduling)**, we achieved significant performance gains.

### 📊 Key Results

| Task                      | Metric     | Baseline (r=8) | NetLLM++ (Ours) | Improvement     |
| :------------------------ | :--------- | :------------- | :-------------- | :-------------- |
| **Video Streaming (ABR)** | QoE Reward | -40.55         | **-37.84**      | **+6.7%**       |
| **Job Scheduling (CJS)**  | Avg JCT    | 66.12s         | **63.14s**      | **4.5% Faster** |

> _Note: Training loss was reduced by 49% (4.89 → 2.46), accelerating convergence on CPU hardware._

---

## 🛠️ Installation & Reproducibility

To reproduce our results on an Intel-based Mac or standard Linux CPU environment, follow these steps.

### 1. Environment Setup

We use **Conda** to manage dependencies and avoid conflicts with system Python.

```bash
# Create the environment
conda create -n netllm python=3.10
conda activate netllm

# Install Core Dependencies
pip install torch torchvision torchaudio
pip install transformers==4.30.0 peft==0.10.0 accelerate
pip install networkx numpy pandas matplotlib

# Install Legacy Compatibility Shim (For tflearn)
pip install tensorflow-macos

2. Apply PatchesWe have included a patch script to fix the int64 casting error in Gymnasium and the GPT-2 embedding size mismatch (1024 vs 768).Bash# Run the patch script before training
bash scripts/patch_tf_legacy.sh
🏃‍♂️ Running the ExperimentsTask 1: Adaptive Bitrate Streaming (ABR)To train the GPT-2 model with High-Rank LoRA ($r=32$):Bashpython run_plm.py \
  --trace fcc-test \
  --video video1 \
  --plm-type gpt2 \
  --plm-size base \
  --device cpu \
  --adapt \
  --num-epochs 1 \
  --rank 32 \
  --save-checkpoint-per-epoch 1 \
  --test
Task 2: Cluster Job Scheduling (CJS)To train the scheduler with High-Rank LoRA ($r=128$):Bashpython run_plm.py \
  --plm-type gpt2 \
  --plm-size base \
  --device cpu \
  --train \
  --num-iters 1 \
  --rank 128 \
  --save-checkpoint-per-iter 1 \
  --test \
  --state-feature-dim 256
📂 Repository StructureNetLLM-PlusPlus/
├── artifacts/          # Logs, Checkpoints, and Results CSVs
├── data/               # FCC Traces and TPC-H datasets
├── plm_special/        # Custom GPT-2 LoRA Implementation
├── scripts/            # Patch scripts for CPU compatibility
├── run_plm.py          # Main entry point for training
└── README.md           # Project Documentation
🙏 Acknowledgments & CitationThis project is a reproduction and extension of the original NetLLM paper presented at ACM SIGCOMM 2024. We acknowledge the original authors for their open-source contribution.Original Paper Citation:Wu, D. et al. (2024). NetLLM: Adapting Large Language Models for Networking. Proceedings of the ACM SIGCOMM 2024 Conference.If you use our optimized CPU-friendly version, please cite:Ali, I., Raza, B., Khan, F., Shahzad, K. (2025). NetLLM++: Resource-Efficient Fine-Tuning of Small LLMs for High-Frequency Network Control on Consumer Hardware.
```
