import urllib.request as request
import queue,time,math
from concurrent.futures import ThreadPoolExecutor
import threading,sched

maxi=-1
lock=threading.Lock()

exp=0
stt=time.clock()
block=65536*4
BSIZE=16*6
chunks=-1

u="https://fpdl.vimeocdn.com/vimeo-prod-skyfire-std-us/01/830/8/204150149/693533288.mp4?token=58a82dba_0x9008b221be87442c29d85d2c4c01cf99bdfef082&download=1&filename=Leningrad+-+Kolshik-SD.mp4"
def get_chunk(u,i,cache,que,block):
    global lock
    dic = {}
    s="bytes={}-{}"
    dic['User-Agent']="Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36"
    dic['Range']=s.format(block*i,block*i+block-1)
    
    try:
        req = request.Request(u,headers=dic)
        res = request.urlopen(req,timeout=4)
        d = res.read()
        with lock:
            cache[i]=d
            
    except:
        print("Failed:",i)
        que.put(i)

    return d

def write(fh,cache,exp,que):
    global maxi,lock
    wed=time.clock()
    maxi=max(maxi,len(cache))
    while exp in cache:
        d=b''
        with lock:
            d=cache[exp]
        fh.write(d)
        with lock:
            del cache[exp]
        #print(exp,"finished")
        exp+=1
    return exp

def write2(fh,cache,exp,que):
    global maxi,lock
    maxi=max(maxi,len(cache))
    temp=b''
    while exp in cache:
        d=b''
        with lock:
            d=cache[exp]
        temp+=d
        with lock:
            del cache[exp]
        #print(exp,"finished")
        exp+=1
    fh.write(temp)

    return exp

def get_sz(u):
    req = request.Request(u)
    res = request.urlopen(req)
    return int(res.headers.get('content-length'))

def stat(sch):
    global exp,block,chunks
    d=exp*block #Wrong
    v=d/(time.clock()-stt)
    print(d/(2**20)," MB at ",v/(2**10)," KB/s")
    assert chunks>-1
    if exp<chunks:
        sch.enter(1,1,stat,argument=(sch,))
        
max_size=2000
f="e:/bbs.mp4"

s="bytes={}-{}"

que = queue.PriorityQueue()
fh=open(f,"wb")
pool = ThreadPoolExecutor(max_workers=6)
sch = sched.scheduler(time.clock,time.sleep)
cache={}
size = get_sz(u)
print("Size:",size)
chunks=math.ceil(size/block)
    
for i in range(chunks):
    que.put(i)
    
sch.enter(1,1,stat,argument=(sch,))
pool.submit(sch.run)
while True:
    i=0
    if not que.empty():
        i = que.get(timeout=3)
        if i<exp+BSIZE:
            f = pool.submit(get_chunk,u,i,cache,que,block)
        else:
            que.put(i)
            #print("BUFFER FULL")

    exp=write(fh,cache,exp,que)
    if exp>=chunks:
        break
    time.sleep(.040)

fh.close()
pool.shutdown(wait=True)
print("Took ",time.clock()-stt," seconds")
print("MAX cache size : ",maxi)

