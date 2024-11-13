lst = [int(i) for i in input().split()]
ans = []
for i in lst:
    if i % 2 == 0:
        ans.append(i)


for i in range(len(ans) - 1):
    for j in range(len(ans) - 1 - i):
        if ans[j] > ans[j + 1]:
            ans[j], ans[j + 1] = ans[j + 1],ans[j]


print("Наибольший элемент",ans[-1])