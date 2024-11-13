lst = [int(i) for i in input().split()]
max_el = max(lst)
min_el = min(lst)

#без сортировки списка
ins = lst.index(max_el)
insss = lst.index(min_el)
lst[ins] = min_el
lst[insss] = max_el
print(lst)





#с сортировкой списка
for i in range(len(lst) - 1):
    for j in range(len(lst) - 1 -i):
        if lst[j] > lst[j + 1]:
            lst[j], lst[j + 1] = lst[j + 1], lst[j]

min_sort_lst = lst[0]
max_sort_lst = lst[-1]
lst[-1] = min_sort_lst
lst[0] = max_sort_lst
print(lst)


