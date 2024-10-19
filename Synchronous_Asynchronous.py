import requests

def fetch_data(url):
    response = requests.get(url)
    return response.text

data1 = fetch_data("https://www.example.com/data1")
data2 = fetch_data("https://www.example.com/data2")
print(data1)
print(data2)

                Synchronous
--------------------------------------------------
                Asynchronous

import asyncio
import aiohttp

async def fetch_data(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            return await response.text()

async def main():
    data1, data2 = await asyncio.gather(
        fetch_data("https://www.example.com/data1"),
        fetch_data("https://www.example.com/data2")
    )
    print(data1)
    print(data2)

if __name__ == "__main__":
    asyncio.run(main())

