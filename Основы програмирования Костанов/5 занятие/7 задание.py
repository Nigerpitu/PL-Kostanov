a = int(input())
count = 0
while a != 0:
    b = a
    a = int(input())
    if b < a:
        count += 1
        print(count)
