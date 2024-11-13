def is_magic_square(matrix):
    n = len(matrix)

    ta_sum = sum(matrix[0])

    for row in matrix:
        if sum(row) != ta_sum:
            return False

    for col in range(n):
        col_sum = sum(matrix[row][col] for row in range(n))
        if col_sum != ta_sum:
            return False

    main_sum = sum(matrix[i][i] for i in range(n))
    if main_sum != ta_sum:
        return False

    secondary_sum = sum(matrix[i][n - i - 1] for i in range(n))
    if secondary_sum != ta_sum:
        return False

    return True

matrix = [
    [8, 1, 6],
    [3, 5, 7],
    [4, 9, 2]
]

if is_magic_square(matrix):
    print("Матрица является магическим квадратом.")
else:
    print("Матрица не является магическим квадратом.")

