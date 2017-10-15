import random
import time
def insertion(a):
    k=0
    for i in range(len(a)):
        k=i
        t=a[i]
        while k>0 and t<a[k-1]:
            a[k]=a[k-1]
            k-=1
        a[k]=t
    print(a)
x=[]
for i in range(100):
    k=random.randint(1,91)
    x.append(k)
s=time.clock()
insertion(x)
k=time.clock()
print(k-s)
