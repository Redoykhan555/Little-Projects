from utils import *
def test():
    to="c:/pyDownLoads"
    fro="h:"
    dic = search("music",fro)
    x=0
    for k in dic:
        f=open(os.path.join(to,k),"rb")
        g=open(os.path.join(fro,k),"rb")
        if f.read()!=g.read():
            print(f,x)
            break
        x+=1
        f.close()
        g.close()
    if x==len(dic):
        print("AWESOME")
    else:
        print(x,len(dic))
test()
