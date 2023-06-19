import time
import os

os.environ['KMP_DUPLICATE_LIB_OK']='True'

out_dir = 'out-lyrics'
eval_interval = 5
eval_iters = 40
wandb_log = False # feel free to turn on
wandb_project = 'lyrics'
wandb_run_name = 'ft-' + str(time.time())

dataset = 'lyrics'
init_from = 'gpt2-xl' # this is the largest GPT-2 model

# only save checkpoints if the validation loss improves
always_save_checkpoint = False

# the number of examples per iter:/finetune_
# 1 batch_size * 32 grad_accum * 1024 tokens = 32,768 tokens/iter
# shakespeare has 301,966 tokens, so 1 epoch ~= 9.2 iters
batch_size = 1
gradient_accumulation_steps = 32
max_iters = 20

# finetune at constant LR
learning_rate = 3e-5
decay_lr = False