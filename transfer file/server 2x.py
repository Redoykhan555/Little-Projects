import os,os.path,json,socket,socketserver,shutil,time


def search(path,dic={},base=""):
    cur = base+"/"+path
    if os.path.isfile(cur):
        dic[path] = os.stat(base+"/"+path).st_size
        return 
    li = os.listdir(cur)
    for f in li:
        if os.path.isdir(cur+"/"+f):
            search(path+"/"+f,dic=dic,base=base)
        else:
            dic[path+"/"+f] = os.stat(cur+"/"+f).st_size
            
def carry_on(wf,dic={},base=""):
    files = sorted(list(dic.keys()))
    for f in files:
        fh = open(base+"/"+f,"rb")
        shutil.copyfileobj(fh, wf)
        
                                      
class Handler(socketserver.StreamRequestHandler):
    def handle(self):
        print("Request from :",self.client_address)
        c=self.request
        rf=c.makefile("rb",-1)
        wf=c.makefile("wb",0)
        
        line = rf.readline(8234)
        line = line.decode()
        fn = line.rstrip()
        print(fn)
        
        path = fn
        path = path.split('/')
        base = '/'.join(path[:-1])
        dic={}
        geer = time.clock()
        search(path[-1],dic=dic,base = base)
        print(time.clock()-geer)
        x=0
        msg = bytes((json.dumps(dic)+'\n'),encoding="utf-8")# IF NEWLINE ALLOWED IN FILENAME, I AM FUCKED
        wf.write(msg)
        
        carry_on(wf,dic,base)
        
            
    
def main():
    ser=socketserver.TCPServer(("",9090),Handler)
    ser.serve_forever()
    
if __name__=='__main__':
    main()
    
    
    
    
    
