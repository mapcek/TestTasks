n = int(input())
m = int(input())

step = 1


while True:
    print(step, end="")
    step = 1 + (step + m - 2) % n
    if step == 1:
        break
print()
