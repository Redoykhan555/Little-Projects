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
        if p.endswith(".h") or p.endswith(".c") or p.endswith(".cpp"):
            return func(p)
        return 0
    li = os.listdir(p)
    for f in li:
        ans=ans+search(os.path.join(p,f))
    return ans

p="C:/Users/user/Google Drive/source codes/Stockfish-master"
print(search(p))
