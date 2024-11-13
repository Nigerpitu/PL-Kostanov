lst = [1, 2, 3, 4, 5, 2, 6, 7, 8, 9, 3]


lst_Pov = []


for i in range(len(lst)):
    for j in range(i + 1, len(lst)):
        if lst[i] == lst[j] and lst[i] not in lst_Pov:
            lst_Pov.append(lst[i])


if lst_Pov:
    print("Повторяющиеся элементы:", lst_Pov)
else:
    print("Повторяющихся элементов нет.")
