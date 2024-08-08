import sys
input = sys.stdin.readline

n = int(input())

def cal(lst):
    top = 0
    result = 1
    for i in range(1,len(lst)):
        if lst[top] > lst[i]:
            top = i
            result+=1
    return result

put = []
for _ in range(n):
    m = int(input())
    g = [0]*m
    for _ in range(m):
        f, m = map(int,input().split())
        g[f-1] = m
    put.append(g)


for lst in put:
    print(cal(lst))
