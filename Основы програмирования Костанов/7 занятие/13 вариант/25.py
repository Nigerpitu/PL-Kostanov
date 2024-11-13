lst = [int(i) for i in input().split()]
duplic = []


for i in range(len(lst)):
    curr_z = lst[i]
    curr_i = [i]
    for j in range(i + 1, len(lst)):
        if lst[j] == curr_z:
            curr_i.append(j)

    if len(curr_i) > 1:
        if curr_z not in [item[0] for item in duplic]:
            duplic.append((curr_z, curr_i))

if duplic:
    for value, indices in duplic:
        print(f"Элемент {value} встречается на индексах {indices}")
else:
    print("Повторяющихся элементов не найдено.")
