def failure_function(pattern):
    m=len(pattern)
    failure_array=[None]*m
    failure_array[0]=0
    k=0
    for q in range(1,m):
        while k>0 and pattern[k]!=pattern[q]:
            k=failure_array[k-1]
        if pattern[k]==pattern[q]:
            k=k+1
        failure_array[q]=k
    return failure_array

def KMP(text,pattern):
    F=failure_function(pattern)
    len_text=len(text)
    len_pattern=len(pattern)
    q=0
    for i in range(len(text)):
        while q>0 and pattern[q]!=text[i]:
            q=F[q]
        if text[i]==pattern[q]:
            q=q+1

        if q==len_pattern:
            print("match at :",i-(len_pattern-1)," index")
            q=F[q-1]

t=input("t")
p=input("p")
KMP(t,p)
        
        
