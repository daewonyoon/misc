def gcd(m, n):
    if m < n:
        m, n = n, m
        g, a, b = gcd_(m, n)
        return g, b, a
    return gcd_(m, n)


def gcd_(m, n):
    # returns g, a, b
    # s.t.   g = a m + b n
    # g is greatest common divider
    # m >= n
    if m % n == 0:
        return n, 0, 1
    g, aa, bb = gcd_(n, m % n)
    # g = aa x ( n ) + bb x ( m%n )
    # m%n = m - (m//n)*n
    # g = aa x n + bb x [ m - (m//n) n] = bb m + (aa - bb (m//n)) n
    a, b = bb, aa - bb * (m // n)
    return g, a, b


for m, n in [(33, 5), (2, 7), (122, 2), (34, 26), (123, 231), (123456789, 123)]:
    g, a, b = gcd(m, n)
    print(f"{g} = {a}x{m} + {b}x{n} = {a*m + b*n}")
