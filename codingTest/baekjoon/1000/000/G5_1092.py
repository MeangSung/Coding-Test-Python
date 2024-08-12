import sys
import heapq

read = sys.stdin.readline

n = int(read())
cranes = sorted(list(map(int,read().split())),reverse = True)
m = int (read())
containers = sorted(list(map(int,read().split())),reverse = True)

res = 0
if cranes[0] < containers[0] :
    print(-1)
else:
    while containers:
        for crane in cranes:
            if containers and crane < containers[-1]:
                continue
            for container in containers:
                if container <= crane:
                    containers.remove(container)
                    break
        res+=1
    print(res)

