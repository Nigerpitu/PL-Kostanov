def swap_first_last_columns(matrix):
    N = len(matrix)

    for i in range(N):
        matrix[i][0], matrix[i][N - 1] = matrix[i][N - 1], matrix[i][0]

    return matrix
