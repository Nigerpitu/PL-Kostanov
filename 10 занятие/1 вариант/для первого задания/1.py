def calculate_sum_and_count(matrix):
    N = len(matrix)
    total_sum = 0
    count = 0

    for i in range(N):
        for j in range(i + 1, N):
            if matrix[i][j] > 0:
                total_sum += matrix[i][j]
                count += 1

    return total_sum, count



def read_matrix_from_file(file_name):
    with open(file_name, 'r', encoding='utf-8') as file:
        matrix = []
        for line in file:
            row = list(map(int, line.split()))
            matrix.append(row)
    return matrix



def write_results_to_file(file_name, total_sum, count):
    with open(file_name, 'w', encoding='utf-8') as file:
        file.write(f"Сумма выше главной диагонали: {total_sum}\n")
        file.write(f"Количество элементов выше главной диагонали: {count}\n")


inp_file = "Костанов_Давид_Гарриевич_У-242_vvod.txt"
out_file = "Костанов_Давид_Гарриевич_У-242_vivod.txt"

matrix = read_matrix_from_file(inp_file)

sum1, count1 = calculate_sum_and_count(matrix)

write_results_to_file(out_file, sum1, count1)