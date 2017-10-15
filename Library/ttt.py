ans=[]
def reduce(x):
    ans=''
    for i in x:
        if int(i)>1:
            ans+='1'
        else:
            ans+=i
    return int(ans)
def res(x):
    global ans
    m=reduce(str(x))
    ans.append(m)
    if m==x:
        return 1
    else:
        x=x-m
        return 1+res(x)
n=int(input())
print(res(n))
for i in ans:
    print(i,end= ' ')
        

        
        
        
        

    
    
    
