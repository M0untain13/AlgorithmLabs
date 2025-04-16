import numpy as np


def strassen_multiply(A, B):
    """
    Умножение матриц алгоритмом Штрассена (рекурсивная часть)
    """
    n = A.shape[0]
    # Базовый случай: матрицы 1x1
    if n == 1:
        return A * B
    # Разбиваем матрицы на подматрицы
    mid = n // 2
    A11 = A[:mid, :mid]
    A12 = A[:mid, mid:]
    A21 = A[mid:, :mid]
    A22 = A[mid:, mid:]
    B11 = B[:mid, :mid]
    B12 = B[:mid, mid:]
    B21 = B[mid:, :mid]
    B22 = B[mid:, mid:]
    # Вычисляем промежуточные матрицы по Штрассену
    P1 = strassen_multiply(A11 + A22, B11 + B22)
    P2 = strassen_multiply(A21 + A22, B11)
    P3 = strassen_multiply(A11, B12 - B22)
    P4 = strassen_multiply(A22, B21 - B11)
    P5 = strassen_multiply(A11 + A12, B22)
    P6 = strassen_multiply(A21 - A11, B11 + B12)
    P7 = strassen_multiply(A12 - A22, B21 + B22)
    # Вычисляем блоки результирующей матрицы
    C11 = P1 + P4 - P5 + P7
    C12 = P3 + P5
    C21 = P2 + P4
    C22 = P1 - P2 + P3 + P6
    # Собираем результат из блоков
    C = np.zeros((n, n), dtype=A.dtype)
    C[:mid, :mid] = C11
    C[:mid, mid:] = C12
    C[mid:, :mid] = C21
    C[mid:, mid:] = C22
    return C


def pad_matrix(M, target_size):
    """
    Дополняет матрицу нулями до нужного размера
    """
    rows, cols = M.shape
    padded = np.zeros((target_size, target_size), dtype=M.dtype)
    padded[:rows, :cols] = M
    return padded


def strassen_matrix_mult(A, B):
    """
    Функция-оболочка для умножения матриц произвольных размеров алгоритмом Штрассена
    """
    # Проверка совместимости размеров
    if A.shape[1] != B.shape[0]:
        raise ValueError("Несовместимые размеры матриц для умножения")
    
    p, q = A.shape
    q, r = B.shape
    
    # Находим ближайшую степень двойки для дополнения
    max_dim = max(p, q, r)
    next_pow2 = 1
    while next_pow2 < max_dim:
        next_pow2 <<= 1
    
    # Дополняем матрицы нулями
    A_padded = pad_matrix(A, next_pow2)
    B_padded = pad_matrix(B, next_pow2)
    
    # Умножаем дополненные матрицы
    C_padded = strassen_multiply(A_padded, B_padded)
    
    # Возвращаем результат нужного размера (обрезаем дополненные нули)
    return C_padded[:p, :r]


# Пример использования
def example():
    # Создаем тестовые матрицы
    A = np.array([[1, 2, 3], [4, 5, 6]], dtype=int)
    B = np.array([[7, 8], [9, 10], [11, 12]], dtype=int)
    print("Матрица A:")
    print(A)
    print("Матрица B:")
    print(B)
    # Умножаем с помощью алгоритма Штрассена
    C = strassen_matrix_mult(A, B)
    print("Результат умножения A x B (Штрассен):")
    print(C)