lst = [int(i) for i in input().split()]
sum_lst = 0
proiz_lst = 1
for i in lst:
    proiz_lst *= i
    sum_lst += i

print(sum_lst,proiz_lst)