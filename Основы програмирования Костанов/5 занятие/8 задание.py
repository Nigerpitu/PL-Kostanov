a = int(input())
count = 1
m = 0
while a != 0:
    b = a
    a = int(input())
    if b == a:
        count += 1
        m = count
        print(count,m)
    else:
        count = 1

print("Наибольшее число подряд идущих элементов этой последовательности равных друг другу",m)