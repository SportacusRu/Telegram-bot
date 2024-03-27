from aiohttp import ClientSession
from src.client.routes import (
    Moderate, Reviews, Places, User
)


class SportacusClient:
    def __init__(self, base_url: str, moderate_key: str) -> None:
        self.__client = ClientSession(base_url)
        self.__moderate_key = moderate_key
    
    @property
    def user(self): return User(self.__client, self.__moderate_key)

    @property
    def moderate(self): return Moderate(self.__client, self.__moderate_key)

    @property
    def reviews(self): return Reviews(self.__client, self.__moderate_key)

    @property
    def places(self): return Places(self.__client, self.__moderate_key)

    async def close(self): await self.__client.close()


def run(): print("run")