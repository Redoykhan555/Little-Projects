import asyncio

async def wr(writer):
    await writer.drain()
    writer.close()

async def handle(reader,writer):
    data = await reader.read(8096)
    writer.write(data[:8024])
    task = asyncio.ensure_future(wr(writer))
    


loop = asyncio.get_event_loop()
coro = asyncio.start_server(handle, '127.0.0.1', 8888, loop=loop)
server = loop.run_until_complete(coro)
loop.run_forever()

