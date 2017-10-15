import asyncio,time

msg = ''.join([chr(i%123) for i in range(1024)])
msg = msg.encode('ascii')

async def connect(loop):
    global msg
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888,
                                                        loop=loop)
    writer.write(msg)
    await writer.drain()
    
    res = 0
    while res<1024:
        temp = await reader.read(1234)
        res += len(temp)
    writer.close()

loop = asyncio.get_event_loop()
x=time.clock()
for i in range(10000):
    loop.run_until_complete(connect(loop))
print(time.clock()-x)
loop.close()
