x = int(input())
y = int(input())

count = 1

while x <= y:
    x = x + (0.1 * x)
    count += 1
    if x >= y:
       print(count)


