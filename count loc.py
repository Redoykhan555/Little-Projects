import os
def func(p):
    f = open(p,"rb")
    x=0
    while True:
        try:
            d=f.readline()
        except UnicodeDecodeError as e:
            print(f)
            raise e
        if not d:
            #print(p,x)
            return x
        x+=1

def search(p):
    ans=0
    if os.path.isfile(p):
        if  p.endswith(".py"):# or p.endswith(".h"): #p.endswith(".c") or p.endswith(".py")
            return func(p)
        return 0
    li = os.listdir(p)
    for f in li:
        ans=ans+search(os.path.join(p,f))
    return ans

p="C:/Users/user/Google Drive/(dum)Best Torrent Client In The world/codes"
print(search(p))
