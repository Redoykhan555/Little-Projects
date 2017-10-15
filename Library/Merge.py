def merge(s1,s2):
    s=[None]*(len(s1)+len(s2))
    i=j=0
    while i+j<len(s):
        if j==len(s2) or (i<len(s1) and s1[i]<s2[j]):
            s[i+j]=s1[i]
            i+=1
        else:
            s[i+j]=s2[j]
            j+=1
    print(s)

x=list(map(int,input().split()))
y=list(map(int,input().split()))

merge(x,y)
    
