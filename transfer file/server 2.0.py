import http.server,shutil,time
import socketserver,os,os.path,socket

cur=os.getcwd().replace("\\","/")

class Handler(socketserver.StreamRequestHandler):
    
    def handle(self):
        global cur
        print("Request from :",self.client_address)
        c=self.request
        rf=c.makefile("rb",-1)
        wf=c.makefile("wb",0)
        line=rf.readline(1234)
        line=line.decode()
        fn=line.rstrip()
        if fn=="list_dir":
            s=(os.listdir(cur))
            ss=[]
            for k in s:
                if os.path.isdir(k):
                    ss.append(k+"*"+"D")
                else:
                    ss.append(k+"*"+"F")
            ss.append(cur.replace("\\","/"))
            s="#".join(ss)        
            s+="\n"
            wf.write(bytes(s,encoding="utf-8"))

        elif fn.startswith("ch "):
            if fn.endswith(".."):
                os.chdir('/'.join(cur.split('/')[:-1]))
            else:
                os.chdir(fn[3:])
            cur=os.getcwd().replace("\\","/")

        else:
            try:
                file=open(fn,"rb")
                shutil.copyfileobj(file,wf)
            except:
                wf.write(bytes("Fuc off\n",encoding="utf-8"))
            
        wf.flush()
        wf.close()
        c.close()
        print(fn,": sent to ",self.client_address[0])

ser=socketserver.TCPServer(("",9090),Handler)
ser.serve_forever()
