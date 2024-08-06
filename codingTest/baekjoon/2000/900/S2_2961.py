N = int(input())

base = []
for _ in range(N):
    base.append(tuple(map(int,input().split())))

bb = []
sb=[]
def col(idx):
    if idx == N:
        return
    for i in range(idx,N):
        sb.append(base[i])
        bb.append(sb.copy())
        col(i+1)
        sb.pop()

def cal():
    minn = int(1e9)
    for i in bb:
        ts = 1
        tb = 0
        for j in i:
            s,b = j[0],j[1]
            ts *= s
            tb += b
        minn = min(minn,abs(ts-tb))
    return minn

col(0)
print(cal())

