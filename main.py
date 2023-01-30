# def main1():
#     n = 8  # размерность матрицы
#     matrix = [[0 for _ in range(n)] for _ in range(n)]
#     fill = 0
#
#     # заполняем матрицу подряд
#     for i in range(n):
#         for j in range(n):
#             matrix[i][j] = fill
#             fill += 1
#
#     # разворачиваем нечетные по индексам строки
#     for i in range(n):
#         if i % 2 != 0:
#             matrix[i].reverse()
#
#     # отзеркалеваем матрицу
#     matrix2 = [[0 for _ in range(n)] for _ in range(n)]  # создаем новую матрицу в которую полноценно развернем получившуюся
#     for i in range(n):
#         for j in range(n):
#             matrix2[i][j] = matrix[j][i]
#
#     # Вывод
#     for rows in range(n):
#         for cols in range(n):
#             print(str(matrix2[rows][cols]).ljust(3), end='')
#         print()
#
#
# def main2():
#     n = 8  # размерность матрицы
#     matrix = [[0 for _ in range(n)] for _ in range(n)]
#     fill = 0
#
#     # заполняем матрицу подряд
#     for i in range(n):
#         for j in range(n):
#             matrix[i][j] = fill
#             fill += 1
#
#     # разворачиваем четные по индексам строки
#     for i in range(n):
#         if i % 2 == 0:
#             matrix[i].reverse()
#
#     # Вывод
#     for rows in range(n):
#         for cols in range(n):
#             print(str(matrix[rows][cols]).ljust(3), end='')
#         print()
#
#
# def main3():
#     n = 8  # размерность матрицы
#     matrix: list = [[0 for _ in range(8)] for _ in range(8)]
#     total = 0  # определяет сумму индексов на четность, значение 0 потому что точка старта [0, 0]
#     fill = 0  # наш счётчки до 63
#     i, j = 0, 0  # индексы матрицы
#     limi, limj = 0, 0  # лимиты для i и j
#
#     while fill <= 63:
#         while total % 2 == 0:  # заполнение диагональю вверх вправо
#             matrix[i][j] = fill
#             fill += 1
#             if fill == 64: break  # Выход из цикла как только последняя ячейка матрицы заполнится
#             if i == limi and j == total:  # блок индексации, пока total меньше размерности матрицы
#                 total += 1
#                 j += 1
#                 if total > 7:
#                     i += 1
#                     j -= 1
#                 break
#             i -= 1
#             j += 1
#             if j == n and i == limi:  # блок индексации, когда total больше размерности матрицы
#                 limi += 1
#                 limj += 1
#                 i += 2
#                 j -= 1
#                 total += 1
#                 break
#         while total % 2 == 1:  # заполнение диагональю вниз влево
#             matrix[i][j] = fill
#             fill += 1
#             if j == limj and i == total:  # блок индексации, пока total меньше размерности матрицы
#                 total += 1
#                 i += 1
#                 if total > 7:
#                     i -= 1
#                     j += 1
#                 break
#             i += 1
#             j -= 1
#             if i == n and j == limj:  # блок индексации, когда total больше размерности матрицы
#                 limj += 1
#                 limi += 1
#                 j += 2
#                 i -= 1
#                 total += 1
#                 break
#
#     # Вывод
#     for rows in range(n):
#         for cols in range(n):
#             print(str(matrix[rows][cols]).ljust(3), end='')
#         print()
#
#
# if __name__ == "__main__":  # конструкция с точкой входа
#     main1()
#     print()
#     main2()
#     print()
#     main3()

def dec(num: str, cc: int) -> int:
    answer, k = 0, 0
    for i in range(len(num) - 1, -1, -1):
        if num[i] in nums:
            answer += int(int(num[i]) * cc ** k)
        else:
            answer += int(alp[num[i]] * cc ** k)
        k += 1
    return answer


def decFloat(num: str, cc: int) -> float:
    answer, k = 0, -1
    for i in num:
        if i in nums:
            answer += int(i) * cc ** k
        else:
            answer += alp[i] * cc ** k
        k -= 1
    return answer


def getSymbol(num):
    if num < 10:
        return num
    return alp[str(num)]


def toCC(num: int, cc: int) -> str:
    r = ''
    while num > 0:
        r = str(getSymbol(num % cc)) + r
        num //= cc
    return r


def getList(num: str, cc: int) -> list:
    if int(num[:2]) < cc:
        l = [int(num[:2]), int(num[2:])]
    else:
        l = [int(num[0]), int(num[1:])]
    return l


def toCC_float(num: float, cc: int) -> str:
    r = ''
    num = int(str(num).replace('0.', '', 1))
    for i in range(5):
        n = getList(str(num * cc), cc)
        r = str(getSymbol(n[0])) + r
        num = n[1]
        if num == 0:
            break
    return r


def main():
    int_num, float_num = input().split(',')
    cc_start, cc_end = int(input()), int(input())
    global alp, nums
    alp = {'A': 10, 'B': 11, 'C': 12, 'D': 13, 'E': 14, 'F': 15, 'G': 16, 'H': 17, 'I': 18, 'J': 19, 'K': 20, 'L': 21, 'M': 22, 'N': 23, 'O': 24, 'P': 25, 'Q': 26, 'R': 27, 'S': 28, 'T': 29, 'U': 30, 'V': 31, 'W': 32, 'X': 33, 'Y': 34, 'Z': 35}
    nums = '0123456789'
    dec_num, dec_float = dec(int_num, cc_start) + int(decFloat(float_num, cc_start)), decFloat(float_num, cc_start)
    print(dec_float)
    *args, dec_float_num = list(map(int, str(dec_float).split('.')))
    cc_num, cc_float = toCC(dec_num, cc_end), toCC_float(dec_float_num, cc_end)[:4]

    print(cc_num + ',' + cc_float)


if __name__ == '__main__':
    main()
