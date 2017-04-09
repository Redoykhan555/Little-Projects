from utils import *
import http.server,shutil,time,json
import socketserver,os,os.path,socket,threading

offset_mgr = ServerOffsetManager()
CHUNK_SZ=1048576
f=1

class ThreadedServer(socketserver.ThreadingMixIn,socketserver.TCPServer):
    def __init__(self,a,b,c):
        self.offset_mgr=c
        super().__init__(a,b)

def get_chunk(path,piece):
    global offset_mgr,CHUNK_SZ
    
    file,offset = offset_mgr.calc_offset(path,piece,CHUNK_SZ)

    base = '/'.join(path.split("/")[:-1])
    
    fh = open(base+'/'+file,"rb")
    fh.seek(offset)
    
    to_send = CHUNK_SZ
    data=b''
    
    while to_send:
        temp=fh.read(to_send)
        data=data+temp
        to_send = to_send-len(temp)
        fh.close()
        
        if to_send:
            file = offset_mgr.next_file(path,file)
            if file=="": #last chunk
                print("LAST PIECE IS:",piece)
                break
            fh = open(base+'/'+file,"rb")
    return data

def send_meta(path,wf):
    global offset_mgr

    dic = offset_mgr.get_dict(path)
    s = json.dumps(dic)+"\n"
    s=bytes(s,encoding="utf-8")
    wf.write(s)
    wf.close()
    
    
class Handler(socketserver.StreamRequestHandler):
    def handle(self):
        global f
        req = self.request
        if f:
            print("Request from ",req)
            f=0
        rf = req.makefile("rb",-1)
        wf = req.makefile("wb",0)
        abdar = rf.readline(4096).decode().rstrip() #request should not cross more than 4KB
        abdar=json.loads(abdar)
        
        if abdar['method']=='GET':
            data=get_chunk(abdar['path'],abdar['piece'])
        
            wf.write(data)
            wf.close()

        elif abdar['method']=='HELLO':
            send_meta(abdar['path'],wf)

        rf.close()

def main():                        
    
    server=ThreadedServer(("",7090),Handler,offset_mgr)
    server_thread = threading.Thread(target=server.serve_forever)
    server_thread.daemon = True
    server_thread.start()

    server_thread.join()


        
if __name__=='__main__':
    main()















    
