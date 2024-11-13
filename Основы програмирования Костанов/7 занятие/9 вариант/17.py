lst = [float(i) for i in input().split()]

lst_New = min([abs(i) for i in lst])


lst.reverse()

print(lst_New,lst)