def reverse_number(n):
    if n < 0:
        print("-", end="")
        reverse_number(-n)
        return

    if n < 10:
        print(n, end="")
        return

    print(n % 10, end="")
    reverse_number(n // 10)


number = 12345
print("Исходное число:", number)
print("Число в обратном порядке:", end=" ")
reverse_number(number)