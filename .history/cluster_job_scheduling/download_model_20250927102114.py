# Create this file in the current directory
# download_model.py
import os
from transformers import LlamaForCausalLM, LlamaTokenizer

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
# This is the EXACT path specified in the README
save_directory = "../../downloaded_plms/llama2/base"
os.makedirs(save_directory, exist_ok=True)

print(f"Downloading model '{model_name}' to '{save_directory}'...")
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name)
tokenizer.save_pretrained(save_directory)
model.save_pretrained(save_directory)
print("Model downloaded successfully.")
