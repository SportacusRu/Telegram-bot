from src.client.routes import BaseRouter


class Reviews(BaseRouter):
    __BASE = "/reviews"

    async def remove(
        self, 
        review_id: int
    ) -> None: 
        return await self.__post(
            "/remove", review_id=review_id
        )