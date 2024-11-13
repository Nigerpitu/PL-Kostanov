n = int(input())
i = 0
count = -1
while i <= n:
    i += 1
    b = bin(i)[2:]
    if b.count("1") == 1:
        count += 1
        print(i,b,count)
