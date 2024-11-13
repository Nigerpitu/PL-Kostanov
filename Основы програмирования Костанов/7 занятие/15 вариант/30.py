lst = [int(i) for i in input().split()]

lst_New = [num for num in lst if num % 2 != 0]



if lst_New:
    lst_New.sort(reverse=True)
    print("Массив нечетных чисел в порядке убывания:", lst_New)
else:
    print("Нечетных чисел нет.")
