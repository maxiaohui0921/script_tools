#-*-coding:utf-8-*-
#__author__='maxh'
import asyncio

class Reader():

    def __init__(self):
        self.count = 0

    async def readline(self):
        await asyncio.sleep(1)
        self.count+=1
        if self.count==100:
            return None
        return self.count

    def __aiter__(self):
        return self

    async def __anext__(self):
        var = await self.readline()
        if var==None:
            raise StopAsyncIteration
        return var

async def fun():
    r = Reader()
    async for item in r:
        print(item)

if __name__ == "__main__":
    asyncio.get_event_loop().run_until_complete(fun())