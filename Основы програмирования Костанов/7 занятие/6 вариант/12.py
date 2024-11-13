lst = [int(i) for i in input().split()]

lst_New = sum([i for i in lst if i > 5])

print(lst_New)