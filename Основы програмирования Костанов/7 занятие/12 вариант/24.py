
A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]



for i in range(len(A)):
    A[i], B[i] = B[i], A[i]


print("Преобразованный массив ", A)
print("Преобразованный массив ", B)