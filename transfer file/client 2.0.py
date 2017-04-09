import http.server,shutil,time
import socketserver,os,os.path,socket

h,p="192.168.42.115",9090
home="c:/pyDownloads"
dic={}

def send_msg(msg):
    s=socket.socket()
    s.connect((h,p))
    rf=s.makefile("rb",-1)
    wf=s.makefile("wb",0)
    msg=msg+"\n"
    msg=bytes(msg,encoding="utf-8")
    wf.write(msg)
    wf.flush()
    wf.close()
    return (s,rf)

def ch_dir(name):
    s,rf=send_msg("ch "+name)
    s.close()
    rf.close()
    
def list_dir():
    global dic,cur
    s,rf=send_msg("list_dir")
    ret=rf.readline(65337)
    reply=ret.decode().rstrip().split("#")
    cur=reply.pop()
    dic={}
    for f in reply:
        a,b=f.split('*')
        dic[a]=b
    rf.close()
    s.close()
    print(cur," : ")
    return reply

def get_file(src,dst):
    s,rf=send_msg(src)
    file=open(dst,"wb")
    d=rf.read(1048576)
    while d:
        file.write(d)
        d=rf.read(1048576)
    file.close()
    rf.close()
    s.close()

def get_folder(name):
    global home
    try:
        os.mkdir(home+"/"+name)
    except FileExistsError:
        pass
    home=home+"/"+name
    ch_dir(name)
    li=list_dir()
    for c in li:
        get_content(c.split("*")[0])
    home='/'.join(home.split('/')[:-1])
    ch_dir("..")
    

def get_content(name):
    global home,dic
    list_dir()
    try:
        if dic[name]=='D':
            get_folder(name)
        else:
            get_file(name,home+"/"+name)
    except KeyError:
        print(name)
        print(dic)

while True:
    list_dir()
    print("1.List Directory")
    print("2.Change Directory")
    print("3.Get file/folder")
    print("4.Quit")
    ch=int(input("choose one : "))
    if ch==1:
        print(list_dir())
    elif ch==2:
        n=input()
        ch_dir(n)
    elif ch==3:
        n=input()
        get_content(n)
    elif ch==4:
        print(dic)
    else:
        break
        
print("Disconnected")














