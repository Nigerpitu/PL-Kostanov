sum = 0
count = 0
while True:
    a = int(input())
    count += 1
    sum += a
    if a == 0:
        print(count - 1, sum / (count - 1))
        break