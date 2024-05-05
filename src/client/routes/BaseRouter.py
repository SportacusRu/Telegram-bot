from typing import Dict
from aiohttp import ClientSession


class BaseRouter:
    __BASE = ""
    def __init__(self, client: ClientSession, moderate_key: str) -> None:
        self.__client = client
        self.__moderate_key = moderate_key

    async def _get(self, url: int, **params: Dict[str, str]):
        async with self.__client.get(
            self.__BASE+url, params=self.__params_add_key(params)
        ) as response:
            return await response.json()
        
    async def _post(self, url, **params: Dict[str, str]):
        print(self.__BASE+url)
        async with self.__client.post(
            self.__BASE+url, params=self.__params_add_key(params)
        ) as response:
            return await response.json()
        
    def __params_add_key(self, params: Dict[str, str]):
        params["moderate_key"] = self.__moderate_key
        return params