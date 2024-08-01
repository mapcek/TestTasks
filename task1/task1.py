import sys

n, m = map(int, sys.argv[1:])

step = 1


while True:
    print(step, end="")
    step = 1 + (step + m - 2) % n
    if step == 1:
        break
