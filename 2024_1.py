def A(n, a, b):
    d = dict()
    for e in a:
        if e not in d.keys():
            d[e] = 0
        d[e] += 1
    for e in b:
        if e not in d.keys():
            d[e] = 0
        d[e] -= 1
    ans = [key for key, value in d.items() if value != 0]
    return ans

def B(n, m):
    dp = [[0 for _ in range(m+1)] for _ in range(m+1)]
    dp[0][n] = 1
    for i in range(m):
        for j in range(m):
            if j - i - 1 >= 0:
                dp[i+1][j-i-1] += dp[i][j] / 2
            if j + i + 1 <= m:
                dp[i+1][j+i+1] += dp[i][j] / 2
            else:
                dp[i+1][m] += dp[i][j] / 2
    ans = 0
    for i in range(m+1):
        ans += dp[i][m]
    return ans

from math import cos, sin, pi
ANGL = pi / 3
def C(p): #!
    p = [(cos(ANGL*i) * p[i], sin(ANGL*i) * p[i]) for i in range(len(p))]
    p = p + p[:2]
    for i in range(len(p)-2):
        va = (p[i+1][0] - p[i][0], p[i+1][1] - p[i][1])
        vb = (p[i+2][0] - p[i][0], p[i+2][1] - p[i][1])
        fi = va[0] * vb[1] - va[1] * vb[0]
        if fi < 0: return 'Non-convex'
    return 'Convex'

def D(a, b, c, end): #!
    r = set()
    def all_variants(a, b, c, t):
        if a == b == c == 0: return
        for va in range(3 if a > 0 else 1):
            for vb in range(3 if b > 0 else 1):
                for vc in range(3 if c > 0 else 1):
                    if va == vb == vc == 0: continue
                    ct = float('inf')
                    if va != 0 and a / va < ct: ct = a / va
                    if vb != 0 and b / vb < ct: ct = b / vb
                    if vc != 0 and c / vc < ct: ct = c / vc
                    r.add(t + ct)
                    all_variants(a - va * ct, b - vb * ct, c - vc * ct, t + ct)
    all_variants(a, b, c, 0)
    return 'Yes' if end in r else 'No'

def E(n, k, a):
    ans = k 
    for e in a:
        ans += e - 1
    return ans

def F(n, p, w, m, d): #! time? O(n**2) нужно переписать перерасчет при отризании, тогда O(n)
    p[0] = 0
    p = [0] + p
    w = [float('inf')] + w
    c = [set() for _ in range(len(p))]
    for i in range(1, len(p)):
        c[p[i]].add(i)

    weights = [0 for _ in range(len(p))]
    def calc_weights(i = 0):
        weights[i] = w[i]
        if len(c[i]) != 0:
            weights[i] += sum(map(calc_weights, c[i]))
        return weights[i]

    def all_children(i):
        if len(c[i]) == 0: return set()
        r = c[i].copy()
        for e in c[i]:
            r |= all_children(e)
        return r

    ans = set(d)
    for e in d:
        ans |= all_children(e)
        c[p[e]].difference_update({e})
    ans = sum([w[e] for e in ans])

    calc_weights()
    while True:
        j = 0
        for i in range(1, len(p)):
            if weights[i] <  weights[j]: j = i
        if weights[j] < 0:
            ans += weights[j]
            c[p[j]].difference_update({j})
            weights = [0 for _ in range(len(p))]
            calc_weights()
        else:
            break

    return ans

def G(n, s):
    d = {'R': 0, 'S': 0, 'P': 0}
    for e in s: d[e] += 1
    t = 'RSPRS'
    ans = float('inf')
    for i in range(len(t) - 2):
        if d[t[i]] != 0 and  (d[t[i+1]] != 0 or d[t[i+1]] == 0 and d[t[i+2]] == 0):
            if d[t[i+1]] + 2 * d[t[i+2]] < ans:
                ans = d[t[i+1]] + 2 * d[t[i+2]]
    return ans

def H(n):
    return 2 * sum([(n - 1) // i for i in range(1, int((n-1)**0.5) + 1)]) - int((n-1)**0.5)**2

def I(n, q): #!
    p = {'__root': None, 'Aaron': '__root', '__None': 'Aaron'}
    c = {'__root': 'Aaron', 'Aaron': '__None', '__None': None}
    for e in q:
        op = e.split()
        if op[0] == 'leave':
            name = op[1]
            p[c[name]] = p[name]
            c[p[name]] = c[name]
            p[name] = None
            c[name] = None
        else:
            name1, op, name2 = op
            if name1 not in p.keys():
                p[name1] = None
                c[name1] = None
            if op == 'after':
                name2 = c[name2]
                p[name1] = p[name2]
                c[name1] = name2 
                c[p[name2]] = name1
                p[name2] = name1
            elif op == 'before':
                p[name1] = p[name2]
                c[name1] = name2 
                c[p[name2]] = name1
                p[name2] = name1
    
    ans = list()
    cur = '__root'
    while True:
        if c[cur] == '__None': break
        ans.append(c[cur])
        cur = c[cur]
    return ans

def J(n, v, q, d):
    v.sort(key=lambda x: -x)
    for i in range(1, len(v)):
        v[i] += v[i-1]

    ans = list()
    for e in d:
        l, r = 0, len(v)
        while l < r:
            c = (l + r) // 2
            if v[c] < e:
                l = c + 1
            else:
                r = c 
        ans.append(l+1)
    return ans


def K(n, s):
    dp = 1
    ans = 1
    for i in range(1, len(s)):
        if s[i] != s[i-1]:
            dp += 1
        else:
            dp = 1
        if dp > ans: ans = dp
    return ans

def L(n, d, m, a):
    a.sort(key=lambda x: x[0])
    s = 0
    c = 0
    for e in a:
        if s + d // e[1] >= n:
            c += e[0] * (n - s)
            return c
        else:
            s += d // e[1]
            c += e[0] * (d // e[1])
    return -1


def M(a, b):
    if a[0] == 'h': a = -int(a.split()[1])
    elif a[0] == 'l': a = int(a.split()[1])
    else: a = 0

    if b[0] == 'h': b = -int(b.split()[1])
    elif b[0] == 'l': b = int(b.split()[1])
    else: b = 0

    if a < b: return f'Chipy-chipy {b - a}'
    if a > b: return f'Chapa-chapa {a - b}'
    return 'together'

def test(ans, fn, args):
    r = fn(*args)
    print(f"{ans == r}: {fn.__name__}{args} -> {r}; ожидалось {ans}")   

if __name__ == '__main__':
    # test([2, 6], A, [5, [1, 2, 3, 4, 5], [4, 3, 6, 1, 5]])
    # test([1, 2], A, [5, [1, 1, 2, 2], [2, 1, 2, 2]])
    # test([11, 12], A, [6, [-5, 2, 10, 11, 12, 20], [20, -5, 12, 12, 2, 10]])

    # test(0.5, B, [1, 3])
    # test(0.026584374625156282, B, [0, 55])
    # test(0.893554687500000000, B, [9, 10])

    # test('Non-convex', C, [[3, 3, 4, 5, 2, 6]])
    # test('Non-convex', C, [[6, 1, 5, 5, 1, 5]])
    # test('Convex', C, [[3, 2, 2, 3, 6, 6]])

    # test('Yes', D, [1, 3, 5, 2])
    # test('No', D, [8, 3, 15, 6])
    # test('Yes', D, [6, 4, 12, 13])

    # test(1, E, [3, 1, [1, 1, 1]])
    # test(10, E, [4, 2, [4, 1, 5, 2]])

    # test(2, F, [8, [1, 1, 1, 1, 2, 3, 3, 4], [1, -2, 1, 5, 4, 0, 2, -3], 2, [3, 5]])
    # test(6, F, [8, [1, 1, 1, 1, 2, 3, 3, 4], [1, -2, 1, 5, 4, 0, 2, -3], 4, [2, 6, 7, 4]])
    # test(6, F, [3, [1, 1, 1], [-2, 4, 4], 2, [2, 3]])

    # test(4, G, [5, list('R P S S P'.split())])
    # test(5, G, [7, list('P S R R P R R'.split())])
    # test(0, G, [3, list('S S S'.split())])

    # test(0, H, [1])
    # test(8, H, [5])
    # test(23, H, [10])

    # test(['Boris', 'Aaron', 'Jacob'], I, [4, ['Din before Aaron', 'Jacob after Aaron', 'Boris after Din', 'leave Din']])
    # ans_i_1 = [
    #     'Masha',
    #     'voenkomat'
    # ]
    # q_i_1 = [
    #     'Roma after Aaron',
    #     'Dima after Roma',
    #     'Masha before Aaron',
    #     'Anton after Roma',
    #     'voenkomat after Anton',
    #     'leave Anton',
    #     'leave Aaron',
    #     'leave Dima',
    #     'leave Roma'
    # ]
    # test(ans_i_1, I, [9, q_i_1])

    # test([2, 1, 4], J, [5, [1, 1, 3, 2, 4], 3, [7, 4, 10]])
    # test([5, 2, 3, 4], J, [8, [10, 2, 8, 9, 14, 12, 9, 5], 4, [50, 18, 31, 40]])

    # test(1, K, [1, '1'])
    # test(3, K, [5, '10010'])
    # test(1, K, [4, '0000'])
    # test(6, K, [9, '011010100'])

    # test(11, L, [4, 10, 3, [[4, 5], [2, 8], [1, 7]]])
    # test(34, L, [10, 5, 4, [[1, 2], [4, 1], [2, 2], [8, 4]]])
    # test(-1, L, [12, 4, 2, [[4, 1], [2, 2]]])
    
    # test('Chapa-chapa 4', M, ['accurately', 'hurry 4'])
    # test('together', M, ['late 10', 'late 10'])
    # test('Chipy-chipy 13', M, ['hurry 8', 'late 5'])

    pass