import http.server,shutil,time
import socketserver,os,os.path,socket

h,p=socket.gethostbyname(socket.gethostname()),9090
home="c:/pyDownloads"
h="192.168.0.108"
dic={}
cur=""

def send_msg(msg):
    f=0
    if msg.startswith("put"):
        f=1
    s=socket.socket()
    s.connect((h,p))
    rf=s.makefile("rb",-1)
    wf=s.makefile("wb",0)
    msg=msg+"\n"
    msg=bytes(msg,encoding="utf-8")
    wf.write(msg)
    if f:
        return (s,rf,wf)
    wf.flush()
    wf.close()
    return (s,rf)

def ch_dir(msg):
    s,rf=send_msg(msg)
    rf.close()
    s.close()
    
def list_dir():
    global dic,cur
    s,rf=send_msg("ls")
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
    file=open(dst,"wb")
    s,rf=send_msg("get "+src)
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
    send_msg("cd "+name)
    
    li=list_dir()
    for c in li:
        get_content(c.split("*")[0])
        
    home='/'.join(home.split('/')[:-1])
    ch_dir("cd ..")
    

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

def upload_file(name):
    try:
        file = open(cur+"/"+name,"rb")
    except:
        print("File path leads to nowhere")
        return

    s,rf,wf=send_msg("put "+name)
    d=file.read(1048576)
    while d:
        wf.write(d)
        d=file.read(1048576)
    wf.flush()
    wf.close()
    rf.close()
    s.close()
    print("uploaded : ",name)


def upload_folder(name):
    li=os.listdir(cur+"/"+name)
    s,rf,wf=send_msg("put "+name+"*")
    for f in li:
        if os.path.isfile(cur+"/"+name+"/"+f):
            upload_file(name+"/"+f)
        else:
            upload_folder(name+"/"+f)

    wf.flush()
    wf.close()
    rf.close()
    s.close()
    
def upload_content(path):
    global cur
    s=path.split("/")
    name=s[-1]
    cur="/".join(s[:-1])
    
    if os.path.isdir(cur+"/"+name):
        upload_folder(name)
    elif os.path.isfile(cur+"/"+name):
        upload_file(name)
    else:
        print("WRONG PATH",path)


print("List Directory : ls")
print("Change Directory: cd _folder_")
print("Download file/folder: get _name_")
print("upload file: put _full path_")
print("Quit: exit")


while True:
    
    command=input(">>")
    if command in ["lss","cd","get","put","exit"]:
        print("Invalid command")
    else:
        
        if command.startswith("ls"):
            print(list_dir())
        elif command.startswith("cd"):
            ch_dir(command)
        elif command.startswith("get"):
            get_content(command[4:])
        elif command.startswith("put"):
            upload_content(command[4:])
            x=0
        else:
            break
        
print("Disconnected")














