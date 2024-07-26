import sys

sys.setrecursionlimit(int(1e6))
read = sys.stdin.readline

n, k = map(int, read().rstrip().split())
tree = {i :[] for i in range(n)}
for _ in range(n-1):
    s, e = map(int, read().rstrip().split())
    tree[s].append(e)
    tree[e].append(s)

line = list(map(int,read().rstrip().split()))
apples = [i for i in line]

def harvest(start,cnt,depth,visited):
    if apples[start]:
        cnt+=1
    if depth > 0:
        for i in tree[start]:
            if not visited[i]:
                visited[i] = 1
                cnt = harvest(i,cnt,depth-1,visited)
    return cnt

visited = [0] * n
visited[0] = 1
print(harvest(0,0,2,visited))