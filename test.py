from itertools import *
from bisect import *

arr = [1,2,3,4,5,6]

print(list(product(arr,repeat=3)))

# from itertools import *
# 순열 permutations(arr, n)
# 조합 combinations(arr, n)
# 중복순열 product(arr, repeat=n)



def insertion_sort(arr):
  for i in range(1,len(arr)):
    cur = arr[i]
    pos = bisect_left(arr,cur,0,i)

    arr = arr[:pos] + [cur] + arr[pos:i] + arr[i+1:]
    
  return arr

arr = [5,2,9,1,5,6]
print(insertion_sort(arr))