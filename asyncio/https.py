import asyncio
import urllib.parse
import sys


async def get_http_obj(url):
    url = urllib.parse.urlsplit(url)
    
    if url.scheme == 'https':
        connect = asyncio.open_connection(url.hostname, 443, ssl=True)
    else:
        connect = asyncio.open_connection(url.hostname, 80)

    reader, writer = await connect
    query = ('GET {path} HTTP/1.0\r\n'
             'Host: {hostname}\r\n'
             '\r\n').format(path=url.path or '/', hostname=url.hostname)
    writer.write(query.encode('latin-1'))

    res = b'hjjh'
    while res:
        res = await reader.readline()
        res = res.rstrip()
    res = await reader.read()
    
    writer.close()
    return res
"""
url = "https://docs.python.org/3/library/asyncio-stream.html"
loop = asyncio.get_event_loop()
task = asyncio.ensure_future(get_http_obj((url))
loop.run_until_complete(task)
f=task.result()
loop.close()
"""
