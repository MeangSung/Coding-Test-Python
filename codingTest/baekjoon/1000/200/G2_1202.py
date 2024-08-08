import sys
import heapq

read = sys.stdin.readline

n,k = map(int,read().split())

jewelries = []
bags = []
for _ in range(n):
    m,v = map(int,read().split())
    heapq.heappush(jewelries,(m,-v))
for _ in range(k):
    bags.append(int(read()))

available_jewelries = []
bags.sort()
count = 0
for bag in bags:
    while jewelries and jewelries[0][0] <= bag:
        m,v= heapq.heappop(jewelries)
        heapq.heappush(available_jewelries,v)
    if available_jewelries:
        count-=heapq.heappop(available_jewelries)
    elif not jewelries:
        break
print(count)
