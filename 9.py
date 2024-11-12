lst = [int(i) for i in input().split()]
ans = []
for i in range(len(lst) - 1):
    if lst[i] < 0 and lst[i + 1] < 0:
        ans.append((lst[i],lst[i+1]))

print(ans)
