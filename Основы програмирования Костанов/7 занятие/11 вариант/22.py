lst = [int(i) for i in input().split()]
lst_New = sorted([i for i in lst if i % 2 == 0 and i < 10])
if len(lst_New) == 0:
    print("Нет таких элементов")
else:
    print(lst_New)
