lst = [float(i) for i in input().split()]

srz_element = sum(lst)/len(lst)

for i in range(len(lst)):
    if lst[i] == 0:
        value = srz_element
        lst[i] = value

print(lst)