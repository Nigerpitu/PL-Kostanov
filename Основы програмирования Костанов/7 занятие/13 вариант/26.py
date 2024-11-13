lst = [int(i) for i in input().split()]


for i in range(len(lst)):
    if lst[i] < 15:
        lst[i] = lst[i] * 2

print("Преобразованный массив", lst)
