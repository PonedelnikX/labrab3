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

def count_zeros_in_area(matrix, area, N, M):
    count = 0
    mid_row = N // 2
    mid_col = M // 2
    if area == 1:
        for i in range(mid_row):
            for j in range(mid_col):
                if matrix[i][j] == 0:
                    count += 1
    elif area == 3:
        for i in range(mid_row + (N % 2), N):
            for j in range(mid_col):
                if matrix[i][j] == 0:
                    count += 1
    return count

def swap_areas_1_2_symmetrically(matrix, N, M):
    mid_row = N // 2
    mid_col = M // 2
    for i in range(mid_row):
        for j in range(mid_col):
            # область 1: [i][j], область 2: [i][M-1-j]
            matrix[i][j], matrix[i][M - 1 - j] = matrix[i][M - 1 - j], matrix[i][j]

def swap_areas_1_2_non_symmetrically(matrix, N, M):
    mid_row = N // 2
    mid_col = M // 2
    for i in range(mid_row):
        for j in range(mid_col):
            # область 1: [i][j], область 2: [j][i]
            if j < mid_row and i < mid_col:
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

def matrix_transpose(matrix, N, M):
    return [[matrix[i][j] for i in range(N)] for j in range(M)]

def matrix_multiply(A, B, N, M, P):
    # A: N x M, B: M x P, result: N x P
    result = [[0 for _ in range(P)] for _ in range(N)]
    for i in range(N):
        for j in range(P):
            for k in range(M):
                result[i][j] += A[i][k] * B[k][j]
    return result

def scalar_multiply(matrix, scalar, N, M):
    return [[matrix[i][j] * scalar for j in range(M)] for i in range(N)]

def matrix_subtract(A, B, N, M):
    return [[A[i][j] - B[i][j] for j in range(M)] for i in range(N)]

def main():
    file_path = "1lab.txt"  # Имя файла с матрицей
    A = read_matrix_from_file(file_path)
    N = len(A)
    M = len(A[0]) if N > 0 else 0
    if any(len(row) != M for row in A):
        print("Ошибка: матрица не прямоугольная или некорректный файл!")
        return

    K = int(input("Введите число K: "))

    print_matrix(A, "Исходная матрица A")

    F = [row[:] for row in A]

    zeros_area1 = count_zeros_in_area(F, 1, N, M)
    zeros_area3 = count_zeros_in_area(F, 3, N, M)
    print(f"Количество нулей в области 1: {zeros_area1}")
    print(f"Количество нулей в области 3: {zeros_area3}")

    if zeros_area1 > zeros_area3:
        print("Количество нулей в области 1 больше, чем в области 3")
        print("Меняем области 1 и 2 симметрично")
        swap_areas_1_2_symmetrically(F, N, M)
    else:
        print("Количество нулей в области 1 не больше, чем в области 3")
        print("Меняем области 1 и 2 несимметрично")
        swap_areas_1_2_non_symmetrically(F, N, M)

    print_matrix(F, "Матрица F после преобразований")

    AT = matrix_transpose(A, N, M)
    print_matrix(AT, "Транспонированная матрица A^T")

    # Для умножения: A (N x M), AT (M x N) => результат N x N
    AAT = matrix_multiply(A, AT, N, M, N)
    print_matrix(AAT, "Результат умножения A*A^T")

    KF = scalar_multiply(F, K, N, M)
    print_matrix(KF, "Результат умножения K*F")

    # Для вычитания: AAT (N x N), KF (N x M) - корректно только если N == M!
    # Если N != M, то нельзя вычитать, выведите предупреждение
    if N == M:
        result = matrix_subtract(AAT, KF, N, M)
        print_matrix(result, "Итоговый результат A*A^T - K*F")
    else:
        print("Внимание: итоговое вычитание невозможно, так как размеры не совпадают (A*A^T - K*F)!")

if __name__ == "__main__":
    main()








