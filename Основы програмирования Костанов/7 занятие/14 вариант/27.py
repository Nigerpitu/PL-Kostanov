lst = [int(i) for i in input().split()]


max_index = list.index(max(lst))
min_index = lst.index(min(lst))

lst[max_index], lst[min_index] = lst[min_index], lst[max_index]

print("Преобразованный массив:", arr)
