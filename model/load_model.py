from huggingface_sb3 import load_from_hub
import torch


# TODO: get from some config idk
state_dict = load_from_hub("vsabov/rl-lab", "ppo-LunarLander-v2.zip")


torch.save(state_dict, "./model/state-dict.pt")
