import http.server,shutil,time,os
import socketserver,os,os.path,socket,json

from concurrent.futures import ThreadPoolExecutor

h,p=socket.gethostbyname(socket.gethostname()),19090
h="192.168.0.102"
dst = "c:"
#msg = "get c:/users/user/google drive/programs"

def send_msg(msg):
    global h,p
    s=socket.socket()
    s.connect((h,p))
    rf=s.makefile("rb",-1)
    wf=s.makefile("wb",0)
    msg=msg+"\n"
    print(msg)
    msg=bytes(msg,encoding="utf-8")
    wf.write(msg)
    wf.flush()
    wf.close()
    return (s,rf)

def prepare(f):
    global dst
    if os.path.exists(dst+"/"+f):
        return open(dst+"/"+f,"wb")
    
    ar = f.split('/')
    x=ar[-1]
    ar=ar[:-1]
    cur = dst
    for v in ar:
        cur=cur+"/"+v
        if not os.path.exists(cur):
            os.mkdir(cur)
    return open(cur+"/"+x,"wb")

def get_files(dic,rf):
    files = sorted(list(dic.keys()))
    x=0
    t=time.clock()
    for f in files:
        fh = prepare(f)
        sz=dic[f]
        while sz:
            d=rf.read(min(sz,1048576))
            fh.write(d)
            sz = sz-min(sz,1048576)
        fh.close()
        x+=sz
        print(f,time.clock()-t)
    rf.close()
        
def get_content(path):    
    sock,rf = send_msg(path)
    temp = json.loads(rf.readline().decode().rstrip())
    dic = {}
    for k,v in temp.items():
        dic[k]=v
    get_files(dic,rf)

ress= time.clock()
get_content("h:/The.Edukators.2004.DVDRip.XviD-QiX")
print(time.clock()-ress)












