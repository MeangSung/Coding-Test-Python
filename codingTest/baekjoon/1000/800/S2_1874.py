n = int(input())

arr = []
next = 1
for i in range(1,n+1):
    num = int(input())
    if next > num:
        print('no')
    else:
        