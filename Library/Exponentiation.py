#find value of x**n
import time
def power(x,n):
    if n==0:
        return 1
    if n==1:
        return x
    elif n%2==0:
        return power(x,n/2)**2
    elif n%2==1:
        p=int(n/2)
        return power(x,p)*power(x,p+1)

"""x=time.clock()

for i in range(0,20):
    power(10,i)
for i in range(0,80):
    power(4,i)   
y=time.clock()"""
print(power(2,7))
