from src.client import SportacusClient
from asyncio import get_event_loop


async def run():
    client = SportacusClient("https://google.com", "")
    await client.close()

if __name__ == "__main__":
    loop = get_event_loop()
    loop.run_until_complete(run())