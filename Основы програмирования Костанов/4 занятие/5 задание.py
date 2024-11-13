n = int(input())
sum = 0
for i in range(n + 1):
    c = i ** 3
    sum += c
    print(sum, c)
print(sum)