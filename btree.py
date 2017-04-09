import time
def comp(node):
    return node.keys[0].k
def pcomp(p):
    return p.k

total=0

class Pair:
    def __init__(self,k,v):
        self.k=k
        self.v=v
    def __repr__(self):
        x=str(self.k)+":"+str(self.v)
        return x

class Node:
    def __init__(self):
        self.keys=[]
        self.ch=[]
        self.p=None
        self.next=None
    def is_leaf(self):
        return len(self.ch)==0

    def add_key(self,tree,k,v):
        self.keys.append(Pair(k,v))
        self.keys=sorted(self.keys,key=pcomp)
        self.ch=sorted(self.ch,key=comp)
        if len(self.keys)>tree.b-1:
            new =Node()
            new.next=self.next
            self.next=new
            to=int(len(self.keys)/2)
            new.keys=self.keys[to:]
            sorted(new.keys,key=pcomp)
            mk=self.keys[to]
            self.keys=self.keys[:to]
            if not self.is_leaf():
                x=to+1
                new.ch=self.ch[x:]
                self.ch=self.ch[:x]
                for c in new.ch:
                    c.p=new
            if self.p==None:
                tree.root=Node()
                tree.root.ch.append(self)
                tree.root.ch.append(new)
                tree.root.add_key(tree,mk.k,mk.v)
                new.p=self.p= tree.root
                
            else:
                self.p.ch.append(new)
                new.p=self.p
                self.p.add_key(tree,mk.k,mk.v)
            if not self.is_leaf():
                    x=[]
                    for pp in new.keys:
                        if pp.k!=mk.k:
                            x.append(pp)
                    new.keys=x
    def __repr__(self):
        return str(self.keys)+str(len(self.ch))

class Tree:
    def __init__(self):
        self.root=None
        self.b=15
        self.size=0

    def traverse(self,a,b):
        node=self.find(a)
        while node!=None:
            for k in node.keys:
                if a<=k<=b:
                    print(k)
                if k>b:
                    return
            node=node.next

    def bfs(self):
        p=[self.root]
        ch=[]
        l=1
        while len(p)>0:
            for c in p:
                print("Level:",l,c)
                for k in c.ch:
                    ch.append(k)
            p=ch
            ch=[]
            l+=1

    def search(self,root,k):
        if root.is_leaf():
            return root
        for i in range(len(root.keys)):
            if k<root.keys[i].k:
                return self.search(root.ch[i],k)
        return self.search(root.ch[-1],k)

    def find(self,v):
        return self.search(self.root,v)

    def insert(self,k,v):
        if self.root==None:
            self.root=Node()
        node=self.find(k)
        node.add_key(self,k,v)
        self.size+=1
		
    def mean(self,k):
        global total
        x=time.clock()
        node=self.find(k)
        for p in node.keys:
            if p.k==k:
                total+=(time.clock()-x)
                return "Found"
        total+=(time.clock()-x)
        return "Not found"
        

tree=Tree()
n=int(input())
dic={}
for i in range(n):
    ll=input()
    k,v=" "," "
    k=ll
    tree.insert(k,v.lower())

m=int(input())
for i in range(m):
	s=input()
	print(s,tree.mean(s))

print(total)














