lst = [int(i) for i in input().split()]

lst_New = []

for i in lst:
    if i not in lst_New:
        lst_New.append(i)

print(lst_New)