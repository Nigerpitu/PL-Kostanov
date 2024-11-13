lst = [int(i) for i in input().split()]
sz_lst = sum(lst)//len(lst)

print(lst)
for i in range(len(lst)):
    if lst[i] == 0:
        lst.pop(i)
        lst.insert(i,sz_lst)


print(lst)