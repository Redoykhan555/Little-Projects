def counting(A,k):
    n=len(A)
    C=[0]*(k+1)
    B=[None]*(n)
    for i in A:
        C[i]=C[i]+1

    for i in range(1,k+1):
        C[i]=C[i]+C[i-1]

    for j in range(n-1,-1,-1):
        B[C[A[j]]-1]=A[j]
        C[A[j]]-=1
    #print(B)
    return B

x=[2,5,3,0,2,3,0,3]
print(x)
counting(x,5)
    
    
