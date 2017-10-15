#takes integer,return a string
def toBinary(x):
    k=0
    m=1
    while m<=x:
        m*=2
        k+=1
    print(k)
    ans=[None]*k
    while x!=0:
        p=x%2
        x=int(x/2)
        ans[k-1]=(str(p))
        k-=1
        print(ans)
    return ''.join(ans)

#takes string, return integer.
def fromBinary(s):
    k=len(s)-1
    ans=0
    while k>=0:
        ans=ans+int(s[k])*(2**(len(s)-k-1))
        k-=1
    return ans
    

print(toBinary(14241))
    
