def max_subarray(A):
    max_ending_here = max_so_far = 0
    for x in A:
        max_ending_here = max(0, max_ending_here + x)
        print(max_ending_here)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

#When len of 0 not allowed
def maxi_subarray(A):
    max_ending_here = max_so_far = A[0]
    for x in A[1:]:
        max_ending_here = max(x, max_ending_here + x)
        max_so_far = max(max_so_far, max_ending_here)
    return max_so_far

p=[13,-3,-25,20,-3,-16,-23,18,20,-7,12,-5,-22,15,-4,7]
s=[12,15,-3,10,11]
k=max_subarray(p)
print(k)
