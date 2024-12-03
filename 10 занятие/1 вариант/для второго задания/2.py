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


def read_matrix_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        matrix = []
        for line in file:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix


def write_matrix_to_file(file_name, matrix):
    with open(file_name, 'w', encoding='utf-8') as file:
        for row in matrix:
            file.write(' '.join(map(str, row)) + '\n')


inp_file = "Костанов_Давид_Гарриевич_У-242_vvod.txt"
out_file = "Костанов_Давид_Гарриевич_У-242_vivod.txt"


matrix = read_matrix_from_file(inp_file)

new_matrix = swap_min_max(matrix)

write_matrix_to_file(out_file, new_matrix)

print("Обработка завершена. Результаты записаны в файл.")