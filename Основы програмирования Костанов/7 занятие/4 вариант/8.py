lst = [int(i) for i in input().split()]
lst_Nechet = []
count = 0
for i in range(len((lst)) - 1):
    if lst[i] % 2 != 0:
        lst_Nechet.append(i)

lst_Nechet_True = sorted(lst_Nechet,reverse=True)
print(lst_Nechet_True if len(lst_Nechet) != 0 else print("Нет подходящих чисел"))


