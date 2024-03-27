from pydantic import BaseModel
from typing import List


class Review(BaseModel):
    review_id: int
    user_id: int
    place_id: int
    description: str
    photos: List[str]