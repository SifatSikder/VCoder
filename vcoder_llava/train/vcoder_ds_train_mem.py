# Adopted from https://github.com/lm-sys/FastChat. Below is the original copyright:
# Adopted from tatsu-lab@stanford_alpaca. Below is the original copyright:
# Make it more memory efficient by monkey patching the LLaMA model with FlashAttn.

# Need to call this before importing transformers.
from vcoder_llava.train.llama_flash_attn_monkey_patch import replace_llama_attn_with_flash_attn

replace_llama_attn_with_flash_attn()

from vcoder_llava.train.vcoder_ds_train import vcoder_ds_train
import warnings
warnings.filterwarnings("ignore")

if __name__ == "__main__":
    vcoder_ds_train()
