n = int(input())
c = 1
sum = 0
for i in range(1,n+1):
    c *= i
    sum += c
    print(c)
print(c,sum)