def merge(array):
    l=len(array)
    if l==1:
        return array
    else:
        ans=[]
        p=int(l/2)
        left=array[:p]
        right=array[p:]
        left=merge(left)
        right=merge(right)
        i=0
        while len(ans)<l:
            if len(left)==0 or len(right)==0:
                ans=ans+left+right
                return ans
            if left[0]<right[0]:
                ans.append(left[0])
                left.pop(0)
            else:
                ans.append(right[0])
                right.pop(0)
            i+=1
        return ans


