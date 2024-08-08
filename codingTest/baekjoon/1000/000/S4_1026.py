import sys
import heapq

read = sys.stdin.readline

n = int(input())

a = list(map(int,read().split()))
b = list(map(int,read().split()))
res = 0

heap_a = []
heap_b = []

for i in range(n):
    heapq.heappush(heap_b, -b[i])
    heapq.heappush(heap_a, a[i])

for i in range(n):
    na = heapq.heappop(heap_a)
    nb = heapq.heappop(heap_b)
    res+= na*(-nb)

print(res)