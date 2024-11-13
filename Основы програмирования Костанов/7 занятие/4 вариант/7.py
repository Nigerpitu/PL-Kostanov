lst = [int(i) for i in input().split()]
elemet_Max = max(lst)
elemet_Max_index = (lst.index(elemet_Max) + 1)
print(elemet_Max, elemet_Max_index)