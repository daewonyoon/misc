#!/usr/bin/python  #########################################
# Programming Challenges ISBN 8979142889
# ---------------------------------------- # problem 51 : Euclid Problem #----------------------------------------
# uva 10104 ######################################### # For given m, n, find a, b such that
#  am + bn = g #########################################
# Date      :   2007.03.31 # Author    :   DwYoon @ simsim nara
# TODO      :   Find (a, b) such that |a|+|b| is minimal and a <= b


def gcd(m, n):
    if m < n:
        m, n = n, m  # m is bigger number
    while m % n != 0:
        m, n = n, (m % n)
    return n


# TODO : -> lambda
def f_w(m, n, a, b):
    return a * m + b * n


cases = [[3, 6], [12, 10], [12, 8], [68, 16], [3456, 1657], [2662, 326]]

for pair in cases:
    m, n = pair
    a, b = n, 0
    g = gcd(m, n)
    print("gcd(%d, %d) = %d" % (m, n, g))
    # start with the value when (a, b) = (n, 0), namely mn
    #  changes (a, b) pair and compare f_w(a, b) with gcd(m, n)
    while f_w(m, n, a, b) != g:
        # print("%dx%d + %dx%d = %d"%(a, m, b, n, f_w(m, n, a, b)))
        if f_w(m, n, a, b) > g:
            a = a - 1  # improvement can be made
        else:
            b = b + 1  # imporvement can be made
    print("# %dx%d + %dx%d = %d" % (a, m, b, n, f_w(m, n, a, b)))
