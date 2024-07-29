import sys
from collections import deque

sys.setrecursionlimit(int(1e6))
read = sys.stdin.readline

n, k = map(int,read().rstrip().split())

tree = [[] for _ in range(n)]
for i in range(n-1):
    p,c = map(int, read().rstrip().split())
    tree[p].append(c)
    tree[c].append(p)
score = list(map(int,read().rstrip().split()))

def dfs(s , d):
    visited[s] = True
    if score[s] == k:
        return d
    for node in tree[s]:
        if not visited[node]:
            result = dfs(node,d+1)
            if result is not None:
                return result
    return None




# def bfs(s,visited):
#     q = deque([s])
#     visited[s] = True
#     depth = 0
#     while q:
#         x = q.popleft()
#         if score[x] == k:
#             return depth
#         for nx in tree[x]:
#             if not visited[nx]:
#                 visited[nx] = True
#                 q.append(nx)
#         print("q : ",q)
#         depth+=1

visited = [False] * n
print(dfs(0,0))