def exp(b,n):
    if n==1:
        return b
    if n%2==0:
        return exp(b**2,int(n/2))
    else:
        return b*exp(b**2,int((n-1)/2))
