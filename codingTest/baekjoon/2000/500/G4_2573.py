import sys
from collections import deque

sys.setrecursionlimit(int(1e6))
read = sys.stdin.readline
directions = [(-1,0),(1,0),(0,-1),(0,1)]

def bfs(i,j,graph,visited,n,m):
    q = deque([(i,j)])
    visited[i][j] = True

    while q:
        x,y = q.popleft()
        for d in directions:
            cx, cy = x + d[0], y+d[1]
            if 0 <= cx < n and 0 <= cy < m and graph[cx][cy] and not visited[cx][cy]:
                visited[cx][cy] = True
                q.append((cx,cy))
def melting(graph,n,m):
    L = []
    for x in range(n):
        for y in range(m):
            if graph[x][y]:
                count = 0
                for d in directions:
                    cx,cy = x+d[0], y+d[1]
                    if 0 <= cx <n and 0 <= cy <m and not graph[cx][cy]:
                        count +=1
                L.append((x,y,count))
    for x,y,w in L:
        graph[x][y] = max(0,graph[x][y] - w)

def start():
    n,m = map(int,read().rstrip().split())
    graph = [list(map(int,read().rstrip().split())) for _ in range(n)]
    finish=False
    year = 0
    while True:
        cnt = 0
        visited = [[False] * m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                if graph[i][j] and not visited[i][j]:
                    bfs(i,j,graph,visited,n,m)
                    cnt+=1
                if cnt >= 2:
                    finish = True
        if all(all(line[i]==0 for i in range(m)) for line in graph):
            finish = True
            year = 0
        if finish:
            break
        melting(graph,n,m)
        year+=1
    return year
print(start())