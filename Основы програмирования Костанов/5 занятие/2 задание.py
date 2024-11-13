a = int(input('Введите целое число n>=2: '))
i = 2
while a > 0:
    if a % i == 0:
        print(i)
        break
    else:
        i += 1
