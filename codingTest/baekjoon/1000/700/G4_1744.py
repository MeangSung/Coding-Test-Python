import heapq

def cal(lst):
    global res
    while lst:
        n1 = lst.pop()
        if lst:
            n2 = lst.pop()
            res += n1+n2 if n1 == 1 or n2 ==1 else n1*n2
        else:
            res+=n1

heap = []
res = 0
n = int(input())
for _ in range(n):
    heapq.heappush(heap,int(input()))

p = []
m = []
while heap:
    n = heapq.heappop(heap)
    (p if n >0 else m).append(n)

m.sort(reverse=True)

cal(p)
cal(m)
print(res)