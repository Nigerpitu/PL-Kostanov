lst_All = [int(i) for i in input().split()]
lst_Polozh = [i for i in lst_All if i > 0]
lst_Ostav = [i for i in lst_All if i <= 0]

print("Список положительных элементов", lst_Polozh, "Список оставшихся", lst_Ostav)
