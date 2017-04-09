import urllib.request as request
import urllib.parse as parse
import os,time

u="http://g5s10.fshare.to/movies06/Series/2016/05/11/The.Wire.S02E06.mp4?h=b1gEle6jztBIfEGhUGbO2Q&e=1486421891"
def get_res(url,a,b,c=32767):
    s='bytes={}-{}'
    dic={}
    dic['User-Agent']='Mozilla/5.0 (Windows NT 6.1; Win64; x64)'
    while True:
        dic['Range']=s.format(a,min(a+c,b))
        req = request.Request(url,headers=dic)
        res = request.urlopen(req)
        d=res.read()
        a=a+c+1
        if a>=b:
            yield d
            return 
        yield d

def get_sz(u):
    res = request.urlopen(u)
    li= res.getheaders()
    for a,b in li:
        if a=='Content-Length':
            return int(b)

    raise Exception("Didn't send length")

def download(url,file):
    size = get_sz(url)
    print(size)
    fsz=0
    fh=None
    if os.path.exists(file):
        fh=open(file,"ab")
        fsz=os.stat(file).st_size
    else:
        fh=open(file,"wb")
    fsz+=308628206
    x=0
    t=time.clock()
    for d in get_res(url,fsz,size-1):
        fh.write(d)
        x+=1
        if x%32==0:
            print(x/32,"MB in ",time.clock()-t)
            t=time.clock()
            
    fh.close()
f="e:/das.mp4"













    
