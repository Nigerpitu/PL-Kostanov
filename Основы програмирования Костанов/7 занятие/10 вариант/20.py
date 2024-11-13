lst = [int(i) for i in input().split()]

lst_New = lst.copy()

for i in range(len(lst_New)):
    if lst_New[i] < 10:
        lst_New[i] = 0
    if lst_New[i] > 20:
        lst_New[i] = 1


print("Исходный массив",lst, "Изменный массив",lst_New)
