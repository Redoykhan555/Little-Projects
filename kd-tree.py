import random
class Nodi:
    def __init__(self,ordinata):
        self.ordinata = ordinata
        self.attr = -1
        self.left = None
        self.right = None

    def __repr__(self):
    	return str(self.ordinata)


def aedificare_lignum(punctorum,altitudo):
    if not punctorum:
    	return None
    k = len(punctorum[0].ordinata)
    ind = altitudo%k

    punctorum = sorted(punctorum,key=lambda x:x.ordinata[ind])
    median = len(punctorum)//2

    ans = punctorum[median]
    ans.attr = ind
    ans.left = aedificare_lignum(punctorum[:median],altitudo+1)
    ans.right = aedificare_lignum(punctorum[median+1:],altitudo+1)
    return ans

def display(node,space):
	if node==None:
		return
	print(space,node)
	display(node.left,space+8*'-')
	display(node.right,space+8*'-')

def test_generate(n,k):
	ans = [0]*n
	for i in range(n):
		ans[i] = Nodi([random.randint(1,20) for i in range(k)])
	return ans

def inserere(root,node):
    ind = root.attr
    if node.ordinata[ind]>root.ordinata[ind]:
        if node.right:
            insert(root.right,node)
        else:
            node.right = node
    else:
        if node.left:
            insert(root.left,node)
        else:
            node.left = node
        

test = test_generate(20,5)
root = aedificare_lignum(test,0)
display(root,'')
test = test_generate(5,5)
for n in test:
    print(n)
    inserere(root,n)
    display(root,'')
    print()






















