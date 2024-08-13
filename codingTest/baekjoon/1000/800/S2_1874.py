n = int(input())

input_arr = []

for _ in range(1,n+1):
    input_arr.append(int(input()))

arr = []
next = 1
res = []
for num in input_arr:
    while next <= num:
        arr.append(next)
        next+=1
        res.append('+')
    if arr[-1] == num:
        arr.pop()
        res.append('-')
    else:
        res = ['No']
        break

for s in res:
    print(s)
