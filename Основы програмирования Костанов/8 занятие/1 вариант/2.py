def sumAndSr(ans):
    summa = sum(ans)
    sr_znah = sum(ans)/len(ans)
    return summa,sr_znah

b_ans = []

for i in range(3):
    lst = [int(i) for i in input().split()]
    b_ans.append(sumAndSr(lst))

print(b_ans)