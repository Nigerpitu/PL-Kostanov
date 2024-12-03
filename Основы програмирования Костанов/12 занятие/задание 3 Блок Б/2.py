def print_odd_numbers():
    num = int(input())

    if num == 0:
        return

    if print_odd_numbers.counter % 2 == 1:
        print(num)

    print_odd_numbers.counter += 1

    print_odd_numbers()


print_odd_numbers.counter = 1

print_odd_numbers()
