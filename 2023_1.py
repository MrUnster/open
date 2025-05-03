# math.gcd()
def gcd(a, b):
    if b > a: a, b = b, a
    if a == 0 and b == 0: return -1
    if b == 0: return a
    return gcd(b, a % b)

def lcm(a, b):
    return a * b / gcd(a, b)

def A(n, s):
    s = list(s)
    for i in range(len(s)-1):
        if s[i] == 'r':
            s[i] = 'rr'
    return ''.join(s)

def B(a, b, c):
    p = sorted([a, b, c])
    s = gcd(p[2] - p[0], p[1] - p[0])
    if s > 1: return 'YES'
    return 'NO'

def C(n, p): # ???
    d = dict()
    for i in range(len(p)):
        for j in range(2):
            if p[i][j] not in d.keys():
                d[p[i][j]] = list()
            d[p[i][j]].append(i)
    ans = [set() for _ in range(len(p))]
    for val in d.values():
        for e in val:
            ans[e] |= set(val)
    return max([len(e) for e in ans])

def D(n, c, p):
    b = [None, None]
    for i in range(len(p)):
        if b[p[i]] == None or c[i] < b[p[i]]:
            b[p[i]] = c[i]
    if None in b: return -1
    return sum(b)

def E(n, a, b, m, d, c):
    c.sort()
    ans = 0
    xp = 0
    gold = 0
    for i in range(len(a)):
        # бой
        xp -= a[i]
        if xp <= 0:
            ans += 1 - xp
            xp = 1
        # награда
        gold += b[i]
        # закуп
        if gold >= d and len(c) > 0:
            gold -= d
            xp += c.pop(-1)
    return ans

def F():
    pass

def G(n, t, s): # ???
    d = dict()
    err = 0
    ans = 0
    for i in range(len(t)):
        if t[i] != s[i]:
            err += 1
            key = t[i] + s[i]
            if key not in d.keys():
                d[key] = 0
            d[key] += 1
            if key[::-1] in d.keys() and d[key[::-1]] > 0:
                d[key] -= 1
                d[key[::-1]] -= 1
                err -= 2
                ans += 1
    return ans + err

def H(n):
    if n == 1: return 1
    return sum([i*4 for i in range(n, 0, -2)])

def I(n, p):
    p = list(p)
    ans = 0
    streak = 0
    for i in range(len(p)):
        if streak == 2:
            streak = 0
            p[i] = '1'
        if p[i] == '0':
            ans += 1
            streak += 1
        else:
            streak = 0
    return ans

def J(n, p):
    p = [[e, 0] for e in p]
    for _ in range(2):
        for i in range(len(p)-1):
            if p[i][0] > p[i+1][0] and p[i][1] < 2 and p[i+1][1] < 2:
                p[i][1] += 1
                p[i+1][1] += 1
                p[i], p[i+1] =  p[i+1], p[i]
    return [e[0] for e in p]

def K(d, pd, s, ps):
    ans = 0
    for i in range(len(ps)):
        cans = 0
        for j in range(len(pd)):
            if (ps[i][0] <= pd[j][0] <= ps[i][1]) or (ps[i][0] <= pd[j][1] <= ps[i][1]) or (pd[j][0] <= ps[i][0] <= pd[j][1]):
                cans += 1
        if cans > ans: ans = cans
    return ans

def L(n, p): # ???
    '''
        В m[i][j] хранится число вариантов набрать больше j баллов за первые i работ включая
        => в m[n][54] хранится число вариантов набрать 55 и больше баллов за n работ.
    '''
    m = [[0 for _ in range(55)] for _ in range(len(p))]
    for j in range(55):
        if p[0] > j: m[0][j] = 1
    for i in range(1, len(p)):
        for j in range(55):
            if p[i] > j: m[i][j] += 1
            m[i][j] += m[i-1][j]
            m[i][j] += m[i-1][max(0, j-p[i])]
    
    return m[-1][-1]

def M(n, m):
    return 'light weight' if n >= m else 'heavy'


def test(ans, fn, args):
    r = fn(*args)
    print(f"{ans == r}: {fn.__name__}{args} -> {r}; ожидалось {ans}")

if __name__ == '__main__':
    # print(A(6, 'privet'))
    # print(A(7, 'traktor'))

    test('YES', B, [2, 8, -1])
    test('YES', B, [6, 10, 6])
    test('NO', B, [10, 8, 5])

    # print(C(3, [[1, 2], [3, 7], [3, 2]]))
    # print(C(3, [[4, 5], [2, 4], [4, 5]]))
    # print(C(2, [[1, 4], [9, 2]]))

    # print(D(4, [1, 2, 5, 3], [0, 0, 1, 1]))
    # print(D(3, [8, 2, 1], [0, 0, 0]))

    # test(11, E, [4, [1, 5, 4, 10], [3, 4, 2, 8], 2, 2, [4, 6]])
    # test(26, E, [10, [2, 1, 2, 10, 9, 8, 4, 6, 9, 1], [7, 10, 10, 10, 7, 4, 7, 4, 8, 10], 6, 15, [8, 9, 8, 9, 7, 3]])

    # print(I(7, '0000101'))
    # print(I(16, '0000100010010110'))

    # test(2, G, [5, 'abbab', 'babba'])
    # test(4, G, [4, 'abcd', 'befr'])
    # test(6, G, [8, 'abcbacbd', 'dabccaab'])

    # print(J(5, [3, 1, 4, 2, 5]))
    # print(J(4, [4, 3, 1, 2]))
    # print(J(9, [10, 4, 2, 9, 10, 2, 1, 5, 4]))

    # test(6, L, [5, [15, 10, 25, 15, 10]])
    # test(0, L, [6, [7, 13, 12, 4, 10, 8]])
    # test(170, L, [8, [10, 12, 15, 10, 35, 25, 10, 14]])

    # print(M(10, 10))
    # print(M(6, 8))

    # print(K(
    #     3,
    #     [[1896, 1920],
    #     [1949, 1973],
    #     [1965, 1991]],
    #     5,
    #     [[1899, 1911],
    #     [1915, 1932],
    #     [1928, 1939],
    #     [1955, 1965],
    #     [1971, 1989]]
    # ))

    pass