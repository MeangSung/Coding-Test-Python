import sys

for line in sys.stdin:
    try:
        A, B = map(int, line.split())
        print(A + B)
    except:
        break
