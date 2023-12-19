from fastapi import FastAPI
from contextlib import asynccontextmanager
import torch
from stable_baselines3 import PPO
from app.models import InputData, OutputData
import numpy as np


ml_models = {}


@asynccontextmanager
async def lifespan(app: FastAPI):
    # Load the ML model
    state_dict = torch.load("./model/state-dict.pt")
    model = PPO.load(state_dict)
    ml_models["ppo"] = model
    yield
    # Clean up the ML models and release the resources
    ml_models.clear()


app = FastAPI(lifespan=lifespan)


@app.post("/api/inference")
def inference(input: InputData) -> OutputData:
    input_array = np.array(list(input.model_dump().values()))
    out, _ = ml_models["ppo"].predict(input_array)
    return {"action": out.item()}
