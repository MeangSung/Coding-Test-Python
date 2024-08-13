n = int(input())

arr = [[] for _ in range(51)]

for _ in range(n):
    s = input()
    if s not in arr[len(s)]:
        arr[len(s)].append(s)
        arr[len(s)].sort()

for a in arr:
    if a:
        for s in a:
            print(s)