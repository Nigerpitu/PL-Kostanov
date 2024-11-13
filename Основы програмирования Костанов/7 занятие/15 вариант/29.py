lst = [int(i) for i in input().split()]

no_dup = []

dup = []

for num in lst:
    if num in lst:
        if num not in dup:
            dup.append(num)
    else:
        no_dup.append(num)

if dup:
    print("Повторяющиеся элементы:", dup)
else:
    print("Повторяющихся элементов нет.")
