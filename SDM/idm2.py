import urllib.request as request
import queue,time,math
from concurrent.futures import ThreadPoolExecutor
import threading

lock=threading.Lock()
u="http://ce.bonabu.ac.ir/uploads/30/CMS/user/file/115/EBook/Introduction.to.Algorithms.3rd.Edition.Sep.2010.pdf"
def get_chunk(u,i,cache,que,block):
    global lock
    dic = {}
    s="bytes={}-{}"
    dic['User-Agent']="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    dic['Range']=s.format(block*i,block*i+block-1)
    
    try:
        req = request.Request(u,headers=dic)
        res = request.urlopen(req)
        d = res.read()
        with lock:
            cache[i]=d
            print(i,"downloaded")
    except:
        print("Failed:",i)
        que.put(i)
    return d

def write(fh,cache,exp,que):

    while exp in cache:
        d=b''
        with lock:
            d=cache[exp]
        fh.write(d)
        with lock:
            del cache[exp]
        print(exp,"finished")
        exp+=1
    return exp

def get_sz(u):
    req = request.Request(u)
    res = request.urlopen(req)
    return int(res.headers.get('content-length'))
            
        
def download(u,f,max_size=2000):
    xx=time.clock()
    block=65536
    s="bytes={}-{}"
    que = queue.PriorityQueue()
    fh=open(f,"wb")
    pool = ThreadPoolExecutor(max_workers=4)
    cache={}
    exp=0
    size = get_sz(u)
    chunks=math.ceil(size/block)
    
    for i in range(chunks):
        que.put(i)
    
    while True:
        i=0
        if not que.empty():
            i = que.get()
            f = pool.submit(get_chunk,u,i,cache,que,block)

        exp=write(fh,cache,exp,que)
        if exp>=chunks:
            break
        time.sleep(.1)

    fh.close()
    pool.shutdown(wait=True)
    print("Took ",time.clock()-xx," seconds")
f="e:/ds.pdf"
download(u,f)
