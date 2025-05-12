from math import factorial as fac
def B(n): # зная решение решал 30мин
    A = [1] * (n+1)
    for i in range(1, n+1):
        A[i] = sum([A[j] * A[i-j-1] for j in range(i)])
    # Формула из интернета
    # for i in range(1, n+1):
    #     A[i] = fac(2*i) // (fac(i) * fac(i) * (i + 1))
    B = sum([fac(2*n) // (fac(2*i) * fac(2*(n-i))) * A[i] * A[n-i] for i in range(n+1)])
    return B % (10**9 + 7)

template = [
    [6, 8, 2, 3, 4, 9, 7, 5, 1],
    [9, 7, 5, 8, 1, 2, 4, 3, 6],
    [4, 3, 1, 5, 7, 6, 8, 2, 9],
    [2, 4, 7, 1, 5, 3, 9, 6, 8],
    [5, 1, 6, 2, 9, 8, 3, 7, 4],
    [3, 9, 8, 7, 6, 4, 2, 1, 5],
    [7, 6, 9, 4, 3, 1, 5, 8, 2],
    [1, 2, 3, 9, 8, 5, 6, 4, 7],
    [8, 5, 4, 6, 2, 7, 1, 9, 3],
]
def swap_row(i1, i2):
    for j in range(9):
        template[i1][j], template[i2][j] = template[i2][j], template[i1][j]
def swap_column(j1, j2):
    for i in range(9):
        template[i][j1], template[i][j2] = template[i][j2], template[i][j1]
def H(m):
    v = list()
    for i in range(9):
        for j in range(9):
            if m[i][j] != 0:
                v.append((i, j, i//3, j//3, m[i][j]))
    if v[0][4] == v[1][4]:
        if v[0][0] == v[1][0] or v[0][1] == v[1][1] or (v[0][2] == v[1][2] and v[0][3] == v[1][3]):
            return -1
    
    for i in range(3):
        for j in range(3):
            if template[v[0][2]*3+i][v[0][3]*3+j] == v[0][4]:
                swap_row(v[0][2]*3+i, v[0][0])
                swap_column(v[0][3]*3+j, v[0][1])
    for i in range(3):
        for j in range(3):
            if template[v[1][2]*3+i][v[1][3]*3+j] == v[1][4]:
                swap_row(v[1][2]*3+i, v[1][0])
                swap_column(v[1][3]*3+j, v[1][1])
    
    return template

def is_valid_sudoku(board):
    # Проверка строк
    for row in board:
        if not is_valid_unit(row):
            return False
    # Проверка столбцов
    for col in zip(*board):
        if not is_valid_unit(col):
            return False
    # Проверка квадратов 3x3
    for i in (0, 3, 6):
        for j in (0, 3, 6):
            square = [board[x][y] for x in range(i, i + 3) for y in range(j, j + 3)]
            if not is_valid_unit(square):
                return False
    return True
def is_valid_unit(unit):
    unit = [i for i in unit if i != 0]  # Игнорируем пустые клетки (0)
    return len(unit) == len(set(unit))  # Проверяем на дубликаты


from math import ceil
def L(l, r):
    l, r = ceil(l**0.5), int(r**0.5)
    lq, lr = l // 1000, l % 1000
    rq, rr = r // 1000, r % 1000
    ans = 4 * (rq - lq)
    if 955 < lr: ans -= 4
    elif 795 < lr: ans -= 3
    elif 205 < lr: ans -= 2
    elif 45 < lr: ans -= 1
    if 955 <= rr: ans += 4
    elif 795 <= rr: ans += 3
    elif 205 <= rr: ans += 2
    elif 45 <= rr: ans += 1
    return ans


def test(ans, fn, args):
    r = fn(*args)
    print(f"{ans == r}: {fn.__name__}{args} -> {r}; ожидалось {ans}")

if __name__ == '__main__':
    # test(2, B, [1])
    # test(10, B, [2])
    # test(70, B, [3])
    # test(56628, B, [6])
    # test(-1, B, [1000])

    H_ans = [
        [6, 8, 2, 3, 4, 9, 7, 5, 1],
        [9, 7, 5, 8, 1, 2, 4, 3, 6],
        [4, 3, 1, 5, 7, 6, 8, 2, 9],
        [2, 4, 7, 1, 5, 3, 9, 6, 8],
        [5, 1, 6, 2, 9, 8, 3, 7, 4],
        [3, 9, 8, 7, 6, 4, 2, 1, 5],
        [7, 6, 9, 4, 3, 1, 5, 8, 2],
        [1, 2, 3, 9, 8, 5, 6, 4, 7],
        [8, 5, 4, 6, 2, 7, 1, 9, 3],
    ]
    H_m = [
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0, 0],
        [1, 0, 0, 0, 0, 0, 0, 0, 0],
    ]
    test(H_ans, H, [H_m])

    # test(1, L, [2025, 2025])
    # test(1, L, [1, 3000])
    # test(2, L, [2025, 42025])
    # test(14, L, [2025, 14122024])
    # test(2024, L, [1, 256014122024])
    pass
