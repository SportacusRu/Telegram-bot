from typing import List
from src.client.routes import BaseRouter


class Places(BaseRouter):
    __BASE = "places"

    async def edit(
        self, 
        place_id: int,
        title: str = "",
        description: str = "",
        category: str = "",
        filters: List[str] = ""
    ): 
        return await self._post(
            "/edit", 
            place_id=place_id,
            title=title, 
            description=description, 
            category=category, 
            filters=filters
        )

    async def remove(
        self, 
        place_id: int
    ) -> None: 
        return await self._post(
            "/remove", place_id=place_id
        )