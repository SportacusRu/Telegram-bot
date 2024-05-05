from src.client.routes import BaseRouter


class User(BaseRouter):
    __BASE = "user"

    async def ban(
        self, 
        user_id: int
    ) -> None: 
        return await self._post(
            "/ban", user_id=user_id
        )