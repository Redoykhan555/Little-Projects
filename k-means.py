import random
from PIL import Image

t=0

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
        
def dist(a,b):
    #return ((a.x-b.x)**2+(a.y-b.y)**2)**.5
    return abs(a.i-b.i)

def clusterify(points,centr):
    for p in points:
        p.d = 999999999999999
        for c in centr:
            if dist(p,c)<p.d:
                p.d = dist(p,c)
                p.c=c
    return points

def find_centre(points):
    global t
    ans = points[0]
    dd=9999999999999999999999
    
    for i in points:
        if abs(t-i.i)<dd:
            dd=abs(t-i.i)
            ans=i
    return ans


def kmeans(points,k):
    global t
    n=len(points)
    n = list(range(n))
    random.shuffle(n)
    centr= [points[n[i]] for i in range(k)]
    print(centr)
    old = None
    maxi = 15
    i = 0
    for p in points:
       t+=p.i
    t=t/len(points)
    
    while True:
        old = centr
        i += 1
        cluster = {}
        
        points = clusterify(points,centr)
        for p in points:
            if p.c in cluster:
                cluster[p.c].append(p)
            else:
                cluster[p.c]= [p]
                
        print(cluster.keys())
        assert len(cluster) == k

        centr = []
        for g in cluster:
            c = find_centre(cluster[g])
            centr.append(c)
        
        assert len(centr) == k

        if i==maxi or old==centr:
            break
        print(i)

def image():
    fp = "e:/witcher 2/comp/2.jpg"
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


image()


