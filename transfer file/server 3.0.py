import http.server,shutil,time
import socketserver,os,os.path,socket

cur=os.getcwd().replace("\\","/")

diction = {}

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
        print(fn)
        if fn=="ls":
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

        elif fn.startswith("cd "):
            if fn.endswith(".."):
                os.chdir('/'.join(cur.split('/')[:-1]))
            else:
                os.chdir(fn[3:])
            cur=os.getcwd().replace("\\","/")

        elif fn.startswith("get "):
            try:
                file=open(fn[4:],"rb")
                shutil.copyfileobj(file,wf)
            except:
                print("PROBLEM WITH FILENAME",fn,file)
                wf.write(bytes("Fuc off\n",encoding="utf-8"))
        elif fn.startswith("put "):
            if 6==6:
                path=fn[4:]
                if path[-1]=='*':
                    try:
                        os.mkdir(path[:-1])
                    except FileExistsError:
                        pass
                else:
                    file=open(path,"wb")
                    d=rf.read(1048576)
                    while d:
                        file.write(d)
                        d=rf.read(1048576)
                    file.close()
                
        else:
            print("Problem with command :",fn)
            wf.write(bytes("Fuckk off\n",encoding="utf-8"))
            
        wf.flush()
        wf.close()
        rf.close()
        c.close()
        print(fn,": sent to ",self.client_address[0])

ser=socketserver.TCPServer(("",9090),Handler)
ser.serve_forever()
