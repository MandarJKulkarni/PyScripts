import aiohttp
import asyncio


async def send_request_get_response(url, session):
    for i in range(4):
        async with session.get(url) as resp:
            print(await resp.text())
            # return await resp.read()


async def main():
    async with aiohttp.ClientSession() as session:
        future1 = asyncio.ensure_future(send_request_get_response('http://google.com', session))
        future2 = asyncio.ensure_future(send_request_get_response('http://httpbin.org/get', session))
        # the sequence of responses is async
        # i.e. different from the sync responses: first 4 from google and then 4 responses from httpbin
        await future1
        await future2

if __name__ == "__main__":
    asyncio.run(main())
