import sys,time
from pathlib import *
ss=time.clock()
sys.setrecursionlimit(10000)
dic={}
no=0
def count(drive):
    global dic,no
    p=None
    try:
        p=Path(drive)
    except:
        m=1
        print(drive," Not exist")
        return -1 
    for x in p.iterdir():
        try:
            if x.is_file():
                dic[x.suffix.lower()]=dic.get(x.suffix.lower(),0)+1
            else :
                count(str(x))
        except:
            no+=1
    return 0

count("D:/")
count("C:/")
count("E:/")
count("F:/")
count("G:/")

tot=0
for i in dic:
    tot+=dic[i]
    
di=sorted([(v,k) for (k,v) in dic.items()],reverse=True)
di=[(b,a) for (a,b) in di]
fn=time.clock()

print(di)
print("Total files ",tot)
print("Permission denied: ",no)
print(fn-ss)
