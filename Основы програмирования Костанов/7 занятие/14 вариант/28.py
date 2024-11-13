lst = [int(i) for i in input().split()]
sr_zna = sum(lst) / len(lst)


for i in range(len(lst)):
    if lst[i] > sr_zna:
        lst[i] = 1

print("Среднее арифметическое:", sr_zna)
print("Преобразованный массив:", lst)
