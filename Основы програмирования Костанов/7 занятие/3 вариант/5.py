lst = [int(i) for i in input().split()]
lst_Sum = sum([i for i in range(len(lst)) if i % 2 != 0])
print("Массив D", lst, "Полученная сумма", lst_Sum)