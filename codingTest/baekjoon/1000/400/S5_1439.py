import sys
read = sys.stdin.readline

string = read().rstrip()
w = ''
cnt = 0
for i in range(len(string)):
    if w != string[i]:
        w = string[i]
        cnt+=1
    else:
        continue
print(int(cnt//2))