import sys
input = sys.stdin.readline

n, p = map(str,input().split())
cnt = 1
while int(n) < int(p):
    if int(p) % 2 ==0:
        p = str(int(p) // 2)
    elif p[-1] == '1':
        p = p[:-1]
    else:
        print(-1)
        break
    cnt+=1
else:
    if int(n) == int(p):
        print(cnt)
    else:
        print(-1)
