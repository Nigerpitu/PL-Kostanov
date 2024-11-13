#если использовать массивы
a = int(input())
d = []
for i in range(a):
    d.append(int(input()))

print(sum(d))

#без массива

n = int(input())
sum = 0
for i in range(n):
    c = int(input())
    sum += c

print(sum)