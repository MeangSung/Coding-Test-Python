# import sys
# import itertools
#
# read = sys.stdin.readline
# result = []
#
# while True:
#     line = list(map(int,read().rstrip().split()))
#     n = line.pop(0)
#     if n == 0:
#         break
#     r = itertools.combinations(line,6)
#     result.append(r)
#
# for i in result:
#     for j in i:
#         for k in j:
#             print(k,end=" ")
#         print()
#     print()
#

import sys

read = sys.stdin.readline

result = []
def dfs(s,t):
    if len(t) == 6:
        line.append(t)
        return
    for i in range(len(s)):
        dfs(s[i+1:],t+[s[i]])

while True:
    s = list(map(int, read().rstrip().split()))
    k = s[0]
    if k == 0:
        break
    line = []
    dfs(s[1:],[])
    result.append(line)

for i in result:
    for j in i:
        for k in j:
            print(k,end=" ")
        print()
    print()

