import asyncio,time
import socket

msg = ''.join([chr(i%123) for i in range(1024)])
msg = msg.encode('ascii')

async def connect(loop):
    global msg
    s = socket.socket()
    await loop.sock_connect(s,('127.0.0.1',8888))
    await loop.sock_sendall(s,msg)
    res = 0
    while res<1024:
        temp = await loop.sock_recv(s,1000)
        res += len(temp)
    s.close()

loop = asyncio.get_event_loop()
x=time.clock()
for i in range(10000):
    loop.run_until_complete(connect(loop))

print(time.clock()-x)
loop.close()
