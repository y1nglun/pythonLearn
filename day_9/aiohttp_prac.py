import aiohttp
import asyncio
import time

start = time.time()
CONCURRENCY = 5  # 设置并发限制为5个

semaphore = asyncio.Semaphore(CONCURRENCY)


async def get(url):
    session = aiohttp.ClientSession()
    async with semaphore:
        async with session.get(url) as response:
            return response


async def request():
    url = 'https://www.httpbin.org/delay/5'
    print('Waiting for ', url)
    response = await get(url)
    print('Get response from', url, 'response', response)


tasks = [asyncio.ensure_future(request()) for _ in range(10000)]
loop = asyncio.get_event_loop()
loop.run_until_complete(asyncio.wait(tasks))

end = time.time()
print('Cost time:', end - start)
