import sys

read = sys.stdin.readline()

n = read.rstrip()
start = int(n)
arr = sorted(list(map(int,read.rstrip())))

for i in range(start+1, 1000000):
    if sorted(list(map(int, str(i)))) == arr:
        print(i)
        break
