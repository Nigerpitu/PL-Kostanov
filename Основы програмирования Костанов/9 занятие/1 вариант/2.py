def swap_min_max(matrix):
    N = len(matrix)
    M = len(matrix[0])

    for i in range(N):
        max_index = matrix[i].index(max(matrix[i]))
        min_index = matrix[i].index(min(matrix[i]))

        matrix[i][0], matrix[i][max_index] = matrix[i][max_index], matrix[i][0]

        if min_index == 0:
            min_index = max_index

        matrix[i][M - 1], matrix[i][min_index] = matrix[i][min_index], matrix[i][M - 1]

    return matrix

B = [
    [3, 5, 1, 7, 2],
    [8, 6, 2, 9, 4],
    [5, 9, 3, 1, 6],
    [2, 4, 7, 3, 8]
]

new_matrix = swap_min_max(B)
print("Матрица после замены")
for row in new_matrix:
    print(row)
