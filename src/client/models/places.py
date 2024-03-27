from pydantic import BaseModel
from typing import List


class Place(BaseModel):
    user_id: int
    place_id: int
    title: str
    geo: str
    description: str
    reviews_list: List[int]
    category: str
    filters: List[str]