from math import sqrt

def gipotenuz(a,b):
    c = sqrt(a ^ 2 + b ^ 2)
    return c
def sravn(a,b):
    if a > b:
        print("Гипотенуза a, больше гипотенузы b")
    else:
        print("Гипотенуза b, больше гипотенузы a")

ans = []

for i in range(2):
    a = int(input())
    b = int(input())
    ans.append(gipotenuz(a,b))

sravn(*ans)