from src.client.models import ModerateGetRequst
from src.client.routes import BaseRouter


class Moderate(BaseRouter):
    __BASE = "/moderate"

    async def get(self): 
        response = await self.__get("/get")
        return ModerateGetRequst.model_validate_json(response)

    async def report(self, text: str) -> None: 
        await self.__post("/report", text=text)