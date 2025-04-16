def add_poly(p1, p2):
    """
    Сложение двух полиномов
    """
    len_diff = len(p1) - len(p2)
    if len_diff > 0:
        p2 = p2 + [0] * len_diff
    elif len_diff < 0:
        p1 = p1 + [0] * (-len_diff)
    return [a + b for a, b in zip(p1, p2)]


def subtract_poly(p1, p2):
    """
    Вычитание двух полиномов
    """
    len_diff = len(p1) - len(p2)
    if len_diff > 0:
        p2 = p2 + [0] * len_diff
    elif len_diff < 0:
        p1 = p1 + [0] * (-len_diff)
    return [a - b for a, b in zip(p1, p2)]


def multiply_poly(p1, p2):
    """
    Умножение полиномов методом Карацубы
    """
    n = max(len(p1), len(p2))
    # Дополняем полиномы нулями до степени 2^k - 1 для эффективного разделения
    if (n & (n - 1)) != 0:  # Если n не степень двойки
        new_len = 1
        while new_len < n:
            new_len <<= 1
        p1 = p1 + [0] * (new_len - len(p1))
        p2 = p2 + [0] * (new_len - len(p2))
        n = new_len
    # Базовый случай
    if n == 1:
        return [p1[0] * p2[0]]
    # Разделяем полиномы на половины
    k = n // 2
    a = p1[:k]
    b = p1[k:]
    c = p2[:k]
    d = p2[k:]
    # Рекурсивно вычисляем произведения
    ac = multiply_poly(a, c)
    bd = multiply_poly(b, d)
    a_plus_b = add_poly(a, b)
    c_plus_d = add_poly(c, d)
    ad_plus_bc = subtract_poly(multiply_poly(a_plus_b, c_plus_d), add_poly(ac, bd))
    # Собираем результат
    result = [0] * (2 * n - 1)
    for i, coeff in enumerate(ac):
        result[i] += coeff
    for i, coeff in enumerate(ad_plus_bc):
        result[i + k] += coeff
    for i, coeff in enumerate(bd):
        result[i + 2 * k] += coeff
    return result


# Пример использования
def example():
    # Полиномы задаются списками коэффициентов от младших к старшим
    # Например, [1, 2, 3] соответствует 1 + 2x + 3x²
    p1 = [1, 2, 3]   # 1 + 2x + 3x²
    p2 = [4, 5]      # 4 + 5x
    product = multiply_poly(p1, p2)
    print(f"{product}")   # [4, 13, 22, 15] соответствует 4 + 13x + 22x² + 15x³