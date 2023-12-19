from pydantic import BaseModel
from typing import Literal


class InputData(BaseModel):
    horizontalPadCoordinate: float = 0
    verticalPadCoordinate: float = 0
    horizontalSpeed: float = 0
    verticalSpeed: float = 0
    angle: float = 0
    angularSpeed: float = 0
    leftLegContact: int = 0
    rightLegContact: int = 0


class OutputData(BaseModel):
    action: Literal[0, 1, 2, 3]
