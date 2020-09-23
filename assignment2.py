from collections import counter

def glove(n,arr):
    n = counter(arr)
    return sum(i//2 for i in n.values())
    
    n = input()
    arr = list(map(int,input().split()))
    print(glove(n,arr))
