lst = [int(i) for i in input().split()]

for i in range(len(lst)):
    if lst[i] < 15:
        value = lst[i] * 2
        lst[i] = value

print(lst)