# import os
# from transformers import GPT2Model, GPT2Tokenizer

# model_name = "gpt2"
# # The path is relative, so it works from any experiment folder
# save_directory = "../downloaded_plms/gpt2/base"
# os.makedirs(save_directory, exist_ok=True)

# print(f"Downloading model '{model_name}' to '{save_directory}'...")
# tokenizer = GPT2Tokenizer.from_pretrained(model_name)
# model = GPT2Model.from_pretrained(model_name)
# tokenizer.save_pretrained(save_directory)
# model.save_pretrained(save_directory)
# print("Model downloaded successfully.")

import os
from transformers import LlamaForCausalLM, LlamaTokenizer

model_name = "TinyLlama/TinyLlama-1.1B-Chat-v1.0"
# This path now matches what the corrected script expects
save_directory = "../../downloaded_plms/llama/base"
os.makedirs(save_directory, exist_ok=True)

print(f"Downloading model '{model_name}' to '{save_directory}'...")
tokenizer = LlamaTokenizer.from_pretrained(model_name)
model = LlamaForCausalLM.from_pretrained(model_name)
tokenizer.save_pretrained(save_directory)
model.save_pretrained(save_directory)
print("Model downloaded successfully.")
