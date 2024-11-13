def evklid(x, y):
    while y:
        x, y = y, x % y
    return x


def divid(A, B, C, D):
    nume = A * D
    denom = B * C
    gevklid = evklid(nume, denom)

    s_numer = nume // gevklid
    s_denom = denom // gevklid

    return s_numer,s_denom




a = int(input())
b = int(input())
c = int(input())
d = int(input())


print(divid(a,b,c,d))