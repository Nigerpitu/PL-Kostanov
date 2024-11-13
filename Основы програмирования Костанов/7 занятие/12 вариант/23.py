lst = [int(i) for i in input().split()]
lst_min_nechet = min([i for i in lst if i % 2 != 0])
print(lst_min_nechet)