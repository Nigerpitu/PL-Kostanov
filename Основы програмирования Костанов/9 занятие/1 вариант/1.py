def calculate_sum_and_count(matrix):
    N = len(matrix)
    sum = 0
    count = 0

    for i in range(N):
        for j in range(i + 1, N):
            if matrix[i][j] > 0:
                sum += matrix[i][j]
                count += 1

    return sum, count


A = [
    [1,  2,  3, -4],
    [-1, 5,  6,  7],
    [2, -3, 8,  9],
    [-2, 3, -1, 4]
]

sum1, count1 = calculate_sum_and_count(A)
print(sum1)
print(count1)

