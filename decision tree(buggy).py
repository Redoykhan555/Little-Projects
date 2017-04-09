import math
import random
arr=[]
mx=[-1]*57

class Node:
    def __init__(self):
        self.res=None
        self.split_point=(None,None)
        self.val = None

def do_mx():
    global arr,mx
    for c in range(57):
        for r in range(len(arr)):
            mx[c]=max(mx[c],arr[r][c])

def build_array(p):
    global arr
    f=open(p)
    arr=[]
    x=0
    for l in f:
        s=l.split(',')
        s[-1]=s[-1][0]
        s=[float(i) for i in s]
        arr.append(s)
        assert len(s)==58
    
    assert len(arr)==4601
    f.close()
    do_mx()
    return arr

def calc_entropy(rows):
    global arr
    n=len(rows)
    assert len(rows)>0
    s=0
    for r in rows:
        if arr[r][-1]==1:
            s+=1

    p1=s/n
    if p1==1 or p1==0:
        return 0
    p2=1-p1
    e = p1*math.log2(p1)
    e+=p2*math.log2(p2)
    return -e

def sort(rows,point):
    global arr
    s1=[]
    s2=[]
    val=arr[point[0]][point[1]]
    for r in rows:
        if arr[r][point[1]]<=val:
            s1.append(r)
        else:
            s2.append(r)
    return (s1,s2)

def split(rows,point):
    global arr
    s1,s2=sort(rows,point)
    if len(s1)==0 or len(s2)==0:
        return 1000

    assert len(s1)+len(s2)==len(rows)
    a=calc_entropy(s1)
    b=calc_entropy(s2)
    ans=(a*len(s1)+b*len(s2))/len(rows)
    return ans

def build_tree(rows):
    """Return a single root Node"""
    global arr
    print(len(rows))
    node=Node()
    col=len(arr[0])-1
    row=len(rows)
    info_gain=-999999999999
    split_point=(None,None)
    entropy = calc_entropy(rows)
    if entropy==0:
        node.res = arr[rows[0]][-1]
        return node
    
    for c in range(col):
        for r in range(row):
            if arr[r][c]==mx[c]:
                continue
            gain=split(rows,(r,c))
            if gain==1000:
                continue
            gain=entropy-gain
            #assert gain>=0
            if gain>info_gain:
                split_point=(r,c)
                info_gain=gain
        
    if split_point[0]==None:
        node.res = arr[rows[0]][-1]
        return node
    
    node.split_point = split_point
    node.val = arr[split_point[0]][split_point[1]]
    s1,s2 = sort(rows,split_point)
    node.left = build_tree(s1)
    node.right = build_tree(s2)
    return node

def test(root,row):
    if root.res!=None:
        return root.res
    r,c=root.split_point
    if row[c]<=root.val:
        return test(root.left,row)
    return test(root.right,row)

def aggr_test(root,p,li):
    global arr
    tp=0
    fp=0
    tn=0
    fn=0
    t=0
    for l in li:
        s=arr[l]
        assert len(s)==58
        a=test(root,s)
        if a==s[-1]:
            if a==1:
                tp+=1
            else:
                tn+=1
        else:
            if a==1:
                fp+=1
            else:
                fn+=1
            
        t+=1
    return (tp,tn,fp,fn,tp+tn,t,(tp+tn)/t*100)
    

p="e:/dbms spambase/spambase.data"
arr = build_array(p)
print("Arr done")
rows = list(range(4000))
random.shuffle(rows)
import time
x=time.clock()
root = build_tree(rows[:1500])
print(time.clock()-x)
print("tree done")
a=aggr_test(root,p,rows[3400:])
s=["tp","tn","fp","fn","ok","total","rate"]
for i in range(len(a)):
    print(s[i],a[i])




