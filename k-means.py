import random
from PIL import Image


mx=[-1]*57
mn=[99999999]*57

dp = {}

class Row:
    def __init__(self,arr):
        self.arr = arr
        self.res = None
        self.c = None
        for i in range(57):
            self.arr[i]=float(self.arr[i])
        
def dist(a,b):
    #return ((a.x-b.x)**2+(a.y-b.y)**2)**.5
    global mx,mn,dp
    if (a,b) in dp:
        return dp[(a,b)]
    ans=0
    for i in range(57):
        t = abs(a.arr[i]-b.arr[i])/(mx[i]-mn[i])*100
        assert 0<=t<=100
        ans+=t

    dp[(a,b)] = ans
    return ans

def clusterify(points,centr):
    for p in points:
        p.d = 999999999999999
        for c in centr:
            if dist(p,c)<p.d:
                p.d = dist(p,c)
                p.c=c
    return points

def find_centre(points):
    avg = [0]*58
    for i in range(57):
        for p in points:
            avg[i] = avg[i]+p.arr[i]
        avg[i] = avg[i]/len(points)
    avg = Row(avg)

    ans = points[0]
    dd=9999999999999999999
    for p in points:
        if dist(p,avg)<dd:
            ans=p
            dd=dist(p,avg)
    return ans


def kmeans(points,k):
    random.shuffle(points)
    centr= points[:k]
    maxi = 10
    i = 0
    
    while True:
        i += 1
        cluster = {}
        
        points = clusterify(points,centr)
        for p in points:
            if p.c in cluster:
                cluster[p.c].append(p)
            else:
                cluster[p.c]= [p]
                
        assert len(cluster) == k
        centr = []
        for g in cluster:
            c = find_centre(cluster[g])
            centr.append(c)
        
        assert len(centr) == k

        if i==maxi :
            return cluster


def ham(g):
    i=0
    for p in g:
        if int(p.arr[-1])== 0:
            i+=1
    print(len(g),i)
    return i/len(g)

def spam():
    global mx,mn
    f = open("spambase.data")
    points = []
    for l in f.readlines():
        p = Row(l.split(','))
        points.append(p)

    for i in range(57):
        for p in points:
            mx[i] = max(mx[i],p.arr[i])
            mn[i] = min(mn[i],p.arr[i])

    cl = list(kmeans(points,2).items())
    g1,g2 = cl[0][1],cl[1][1]
    if ham(g1)<ham(g2):
        g1,g2 = g2,g1
        print("ham changed")
    for p in g1:
        p.res = 0
    for p in g2:
        p.res = 1
    assert len(g1)+len(g2)==len(points)

    r = 0
    for p in points:
        if p.res==int(p.arr[-1]):
            r+=1
    return r/len(points)
    
def aggr():
    s=0
    for i in range(10):
        x=spam()
        print(i,':',x)
        s+=x
    print("Aggregate result :",s/10)

#aggr()        
print("result:",spam())

"""
class Point:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.c = None
        self.d= 99999999999999999999999
    def __repr__(self):
        return "({},{})".format(self.x,self.y)

class Pixel:
    def __init__(self,a):
        self.a=a
        self.i = a[0]*256*256+a[1]*256+a[2]
        self.c=None
        self.d= 99999999999999999999999
    
    def __repr__(self):
        return str(self.a)
def image():
    fp = "e:/witcher 2/comp/7.jpg"
    im = Image.open(fp)
    points = []
    for i in range(im.width):
        for j in range(im.height):
            tup = Pixel(im.getpixel((i,j)))
            points.append(tup)
    print("read")
    print(len(points))
    kmeans(points,5)
    print("converted")
    for i in range(im.width):
        for j in range(im.height):
            try:
                tup = points[i*im.height+j].c.a
            except:
                print(i,j)
            im.putpixel((i,j),tup)
    im.save("e:/witcher 2/comp/out.jpg")
"""















