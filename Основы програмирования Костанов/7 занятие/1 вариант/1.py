list = [int(i) for i in input().split()]
list_revers = list
list_revers.reverse()
print(max(list),*list_revers)
