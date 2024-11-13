lst = [int(i) for i in input().split()]
sr_arifm = sum(lst)/len(lst)

count_mensh = 0
count_bolsh = 0
for i in lst:
    if i < sr_arifm:
        count_mensh += 1
    else:
        count_bolsh += 1

print(count_mensh,count_bolsh)