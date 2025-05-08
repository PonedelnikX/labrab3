def read_matrix_from_file(file_path):
    matrix = []
    with open(file_path, 'r') as file:
        for line in file:
            row = list(map(int, line.strip().split()))
            if row:
                matrix.append(row)
    return matrix

def print_matrix(matrix, title="Matrix"):
    print(f"{title}:")
    for row in matrix:
        print(" ".join(f"{num:4}" for num in row))
    print()

def count_zeros_in_area(matrix, area, N):
    count = 0
    mid = N // 2
    if area == 1:
        for i in range(mid):
            for j in range(mid):
                if matrix[i][j] == 0:
                    count += 1
    elif area == 3:
        for i in range(mid, N):
            for j in range(mid):
                if matrix[i][j] == 0:
                    count += 1
    return count

def swap_areas_1_2_symmetrically(matrix, N):
    mid = N // 2
    for i in range(mid):
        for j in range(mid):
            matrix[i][j], matrix[i][N - 1 - j] = matrix[i][N - 1 - j], matrix[i][j]

def swap_areas_1_2_non_symmetrically(matrix, N):
    mid = N // 2
    for i in range(mid):
        for j in range(mid):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def matrix_transpose(matrix, N):
    return [[matrix[j][i] for j in range(N)] for i in range(N)]

def matrix_multiply(A, B, N):
    result = [[0 for _ in range(N)] for _ in range(N)]
    for i in range(N):
        for j in range(N):
            for k in range(N):
                result[i][j] += A[i][k] * B[k][j]
    return result

def scalar_multiply(matrix, scalar, N):
    return [[matrix[i][j] * scalar for j in range(N)] for i in range(N)]

def matrix_subtract(A, B, N):
    return [[A[i][j] - B[i][j] for j in range(N)] for i in range(N)]

def main():
    file_path = "1lab.txt"  # Имя файла теперь lab1.txt
    A = read_matrix_from_file(file_path)
    N = len(A)
    if any(len(row) != N for row in A):
        print("Ошибка: матрица не квадратная или некорректный файл!")
        return
    if N % 2 != 0:
        print("Ошибка: размер матрицы должен быть чётным!")
        return

    K = int(input("Введите число K: "))

    print_matrix(A, "Исходная матрица A")

    F = [row[:] for row in A]

    zeros_area1 = count_zeros_in_area(F, 1, N)
    zeros_area3 = count_zeros_in_area(F, 3, N)
    print(f"Количество нулей в области 1: {zeros_area1}")
    print(f"Количество нулей в области 3: {zeros_area3}")

    if zeros_area1 > zeros_area3:
        print("Количество нулей в области 1 больше, чем в области 3")
        print("Меняем области 1 и 2 симметрично")
        swap_areas_1_2_symmetrically(F, N)
    else:
        print("Количество нулей в области 1 не больше, чем в области 3")
        print("Меняем области 1 и 2 несимметрично")
        swap_areas_1_2_non_symmetrically(F, N)

    print_matrix(F, "Матрица F после преобразований")

    AT = matrix_transpose(A, N)
    print_matrix(AT, "Транспонированная матрица A^T")

    AAT = matrix_multiply(A, AT, N)
    print_matrix(AAT, "Результат умножения A*A^T")

    KF = scalar_multiply(F, K, N)
    print_matrix(KF, "Результат умножения K*F")

    result = matrix_subtract(AAT, KF, N)
    print_matrix(result, "Итоговый результат A*A^T - K*F")

if __name__ == "__main__":
    main()







