import struct
import cmath
import random

def dct(arr):
    N=len(arr)
    ans=[0]*N
    for k in range(N):
        ans[k]=0
        for n in range(N):
            ans[k]+= arr[n]*cmath.cos(cmath.pi/N*(n+.5)*k)
    return ans

def idct(arr):
    N=len(arr)
    ans=[0]*N
    ans[0]=arr[0]/(cmath.sqrt(2))
    for k in range(N):
        ans[k]=0
        for n in range(N):
            ans[k]+= arr[n]*cmath.cos(cmath.pi/N*n*(k+.5))
        
        ans[k] = ans[k]*2/N
    return ans

arr = [i*4 for i in range(10)]
random.shuffle(arr)
print(arr,'\n')

temp = [i.real for i in dct(arr)]
print(temp,'\n')

w=idct(temp)
w=[int(i.real) for i in w]
print(w)
"""
f = open("bird.bmp","rb")
buffer = f.read()
header = buffer[:54]
h,w = struct.unpack("ii",header[18:26])
data = list(buffer[54:])

data=data[:len(data)//2][::-1]+data[len(data)//2:]

data = b''.join(list(map(lambda x:int(x.real).to_bytes(1,'big'),data)))
g = open("test.bmp","wb")
g.write(header)
g.write(data)
g.close()



"""
