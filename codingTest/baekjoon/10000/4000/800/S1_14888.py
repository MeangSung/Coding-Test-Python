import sys

read = sys.stdin.readline
sys.setrecursionlimit(int(1e6))

n = int(read().rstrip())
line = list(map(int,read().rstrip().split()))
cal = list(map(int,read().rstrip().split()))
result = []

def calculation(s,e,c):
    if c == 0:
        return s+e
    if c == 1:
        return s-e
    if c == 3:
        if s < 0:
            return -((-s)//e)
        return s//e
    if c == 2:
        return s*e

def dfs(arr, total,depth):
    if depth == n-1:
        result.append(total)
        return
    for j in range(4):
        if cal[j]:
            cal[j] -= 1
            dfs(arr[1:],calculation(total,arr[0],j),depth+1)
            cal[j] +=1


dfs(line[1:],line[0],0)
print(max(result))
print(min(result))
