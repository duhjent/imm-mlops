from typing import Union
from fastapi import FastAPI

app = FastAPI()

@app.get('/api/inference')
def inference():
    return 'test'

