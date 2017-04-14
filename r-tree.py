M = 4
import turtle as tur
import random as rand
import queue,time

class Node:
    def __init__(self):
        self.childs = {}
        self.rect = None #tuple((x1,y1),(x2,y2))
        self.par = None
        self.dist = 999999999999999999

    def add(self,r,val):
        if not self.rect:
            self.rect = r
            if self.par:
                self.par.add(self.rect,self)
                
        old_rect = self.rect
        self.rect = union(self.rect,r)     
        self.childs[r] = val
        if self.par:
            self.par.childs.pop(old_rect)
            self.par.add(self.rect,self)

    def bulk_add(self,dic):
        self.childs = {}
        self.rect = None
        for k,v in dic.items():
            self.add(k,v)

    def is_leaf(self):
        for k in self.childs:
            return self.childs[k]==None
        return True

    def __repr__(self):
        return str(self.rect)+"  "+str(list(self.childs.keys()))

def draw(rect,col='black'):
    tur.color(col)
    tur.pu()
    tur.setpos(*rect[0])
    tur.pd()
    tur.setpos(rect[1][0],rect[0][1])
    tur.setpos(*rect[1])
    tur.setpos(rect[0][0],rect[1][1])
    tur.setpos(*rect[0])

def union(r1,r2):
    y1 = min(r1[0][1],r2[0][1])
    x1 = min(r1[0][0],r2[0][0])
    x2 = max(r1[1][0],r2[1][0])
    y2 = max(r1[1][1],r2[1][1])
    return ((x1,y1),(x2,y2))

def area(r):
    p1,p2 = r[0],r[1]
    return (p2[0]-p1[0])*(p2[1]-p1[1])

class RTree:
    def __init__(self):
        self.root = Node()
        self.col = ['red','green','blue']

    def _split(self,dic):
        x,y=None,None
        v=0
        keys = list(dic.keys())
        for a in keys:
            for b in keys:
                t = area(union(a,b))
                if t>v:
                    v = t
                    x,y=a,b 

        f,g = [x],[y]
        for k in keys:
            if area(union(x,k))<area(union(y,k)):
                f.append(k)
            else:
                g.append(k)
        a={k:dic[k] for k in f}
        b={k:dic[k] for k in g}
        return a,b

    def _balance(self,node):
        global M
        if len(node.childs)<=M:
            return
        if not node.par:
            self.root = Node()
            node.par = self.root
            node.par.add(node.rect,node)
            
        node.par.childs.pop(node.rect)
        mate = Node()
        a,b = self._split(node.childs)
        node.bulk_add(a)
        mate.bulk_add(b)
        
        if not node.is_leaf():
            for k in b:
                if b[k]:
                    b[k].par = mate

        
        mate.par = node.par
        node.par.add(node.rect,node)
        node.par.add(mate.rect,mate)
        self._balance(node.par)

    def _find(self,root,rect):
        print(0)
        if root.is_leaf():
            return root
            
        to_inc = 9999999999999999999999
        champ = None
        for r in root.childs:
            temp = area(union(r,rect))-area(r)
            if temp<to_inc:
                to_inc = temp
                champ = root.childs[r]

        return self._find(champ,rect) if champ else root

    def insert(self,rect):
        global M
        print("Inserting ... ",rect)
        node = self._find(self.root,rect)
        node.add(rect,None)
        print(9)
        self._balance(node)

    def search(self,rect):
        pass
    
    def display(self):
        col = ['red','blue','violet']
        li = []
        q = queue.Queue()
        self.root.dist = 0
        q.put(self.root)
        while q.qsize():
            u = q.get_nowait()
            li.append(u)
            for k in u.childs:
                n = u.childs[k]
                if n:
                    q.put(n)
                    n.dist = min(u.dist+1,n.dist)

        li.reverse()
        for n in li:
            draw(n.rect,col[n.dist%len(col)])
            time.sleep(.7)

    def struct(self,root,sp=''):
        print(sp,root)
        for k in root.childs:
            if root.childs[k]:
                self.struct(root.childs[k],'--------'+sp)

def gen_test(n):
    ans=[None]*n
    for i in range(n):
        a=rand.randint(-200,200)
        b=rand.randint(-200,250)
        c=rand.randint(a,a+200)
        d=rand.randint(b,b+200)
        ans[i] = ((a,b),(c,d))
    return ans

tree = RTree()
rs = gen_test(20)
print(rs)
col = ['black']
c=0

for r in range(20):
    draw(rs[r])
    tree.insert(rs[r])
    c+=1

tree.display()

def undo(n):
    for i in range(n):
        tur.undo()
    
"""    
for r in rs:
    #tree.insert(r)

tur.speed(2)
tree.struct(tree.root,'')
tree.display()
"""














        
