import asyncio,time

msg = ''.join([chr(i%123) for i in range(18024)])
msg = msg.encode('ascii')

async def connect(loop,i):
    global msg
    #print(i)
    reader, writer = await asyncio.open_connection('127.0.0.1', 8888,
                                                        loop=loop)
    writer.write(msg)
    await writer.drain()
    #print("written ",i)
    
    res = 0
    while res<1024:
        temp = await reader.read(17234)
        res += len(temp)
    #print("read",i)
    writer.close()

loop = asyncio.get_event_loop()
x=time.clock()
for i in range(2000):
    loop.run_until_complete(connect(loop,i))
print(time.clock()-x)
loop.close()
