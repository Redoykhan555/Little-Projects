from utils import ClientOffsetManager,ulta_dic
import http.server,shutil,time
import socketserver,os,os.path,socket,json,math
from sortedcontainers import SortedDict
import subprocess

h,p=socket.gethostbyname(socket.gethostname()),7090
CHUNK_SZ=1048576
home = "c:/pyDownLoads"
offset_mgr = ClientOffsetManager()
dd=None
z=0

def run_test():
    global home,away,dd
    for k in dd:
        name=home+"/"+k
        f=open(name,"rb")
        g=open(away+'/'+k,"rb")
        if f.read()==g.read():
            print(k,": passed",)
        else:
            print(k,": failed",os.stat(name).st_size," ",os.stat(away+'/'+k).st_size)
        f.close()
        g.close()
        
def send_msg(msg):
    global h,p
    msg=bytes(msg,encoding="utf-8")
    s=socket.socket()
    s.connect((h,p))
    rf=s.makefile("rb",-1)
    wf=s.makefile("wb",0)
    wf.write(msg)
    wf.close()
    return (s,rf)

def prepare(f):
    global home
    if os.path.exists(home+'/'+f):
        return
    
    ar = f.split('/')
    x=ar[-1]
    ar=ar[:-1]
    cur = home
    for v in ar:
        cur=cur+"/"+v
        if not os.path.exists(cur):
            os.mkdir(cur)
   
def initialize(dic,x):
    global home
    for k in dic:
        prepare(k)
        name=home+"/"+k
        f=open(name,"wb")
        f.truncate(dic[k])
        f.close()
        

def get_chunk(path,i):
    global CHUNK_SZ
    info={}
    info['method']='GET'
    info['piece'] = str(i)
    info['path']=path
    s,rf = send_msg(json.dumps(info)+"\n")
    data = rf.read(CHUNK_SZ)
    return data

def place_chunk(path,i,data,dic):
    global CHUNK_SZ,home,z
    file,offset=offset_mgr.calc_offset(path,i,CHUNK_SZ)
    to_place=len(data)
    base = home
    
    fh=open(base+"/"+file,"r+b")
    fh.seek(offset)

    s=0
    while to_place:
        x=min(dic[file]-fh.tell(),to_place)
        fh.write(data[s:s+x])
        fh.close()
        to_place = to_place-x
        s+=x

        if to_place:
            file = offset_mgr.next_file(path,file)
            
            try:
                fh=open(base+"/"+file,"r+b")
            except PermissionError as e:
                print("err:",i,len(data))
                
                raise e
    
def greet_server(path):
    info={}
    info['method']='HELLO'
    info['path']=path
    s=json.dumps(info)+"\n"
    s,rf=send_msg(s)
    reply = rf.readline(1800096).decode().rstrip()

    rf.close()
    s.close()

    dic= json.loads(reply)
    ans=SortedDict()
    for k,v in dic.items():
        ans[k]=int(v)

    return ans

def get_content(path):
    global CHUNK_SZ,dd
    dic = greet_server(path)
    dd=dic
    other = ulta_dic(dic)
    offset_mgr.cache[path]=(dic,other)
    sww=time.clock()
    initialize(dic,0)
    print("To initialize:",time.clock()-sww)
    
    total_sz = other.iloc[len(other)-1]
    total_ch = math.ceil(total_sz/CHUNK_SZ)
    
    for i in range(total_ch):
        data=get_chunk(path,i)
        place_chunk(path,i,data,dic)
    print("Total time:",time.clock()-sww)
    
get_content("e:/youtube-dl-master")      














            
    
    
