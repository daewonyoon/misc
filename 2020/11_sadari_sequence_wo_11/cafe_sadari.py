"""
n개의 0과 1을 배열하는데 1과 1은 연속되지 않게 배열하는 경우를 구하는 코드가 필요합니다. 
(ex) 01010 (가능) 01100(불가능)

"""

from functools import lru_cache


def sadari_bruteforce(n: int):
    """
    모든 n자리 이진수 중에서 11을 포함하지 않는 것
    """
    r = [bin(i)[2:].zfill(n) for i in range(2 ** n) if "11" not in bin(i)]
    return r


@lru_cache
def sadari_(n: int):
    if n == 0:
        return [[], []]
    if n == 1:
        return [["0"], ["1"]]
    if n == 2:
        return [["00", "01"], ["10"]]
    sub = sadari_(n - 1)
    r = [[], []]
    for s in sub[0] + sub[1]:
        r[0].append("0" + s)
    for s in sub[0]:
        r[1].append("1" + s)
    return r


def n_sadari(n: int) -> int:
    sadari = sadari_(n)
    return len(sadari[0]) + len(sadari[1])


for i in range(10):
    print(n_sadari(i))


def sadari(n: int):
    return sum(sadari_(n), [])


print(sadari(3))

print(sadari(5))


print(sadari_bruteforce(5))
