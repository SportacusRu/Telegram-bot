from pydantic import BaseModel
from typing import Union
from src.client.models.places import Place
from src.client.models.reviews import Review

class ModerateGetRequst(BaseModel):
    item: Union[Place, Review]
    complaint_count: int