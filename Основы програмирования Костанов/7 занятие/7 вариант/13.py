lst = [int(i) for i in input().split()]

ans_sum = 0

ans_proiz = 1

for i in range(len(lst)):
    if i % 2 == 0:
        ans_sum += lst[i]
    else:
        ans_proiz *= lst[i]


print(ans_sum,ans_proiz)
