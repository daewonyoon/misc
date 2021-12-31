# Author : DwYoon
# PROJECT EULER
# http://projecteuler.net/index.php?section=problems&id=47
# PROBLEM 47
import time


def GetNFactors0(n, primes, _, factors):
    """
    stupid
    """
    sqrtn = int(n ** 0.5) + 1

    for p in primes:
        # p = primes[i]
        if p > sqrtn:
            break
        if n % p == 0:
            f = factors[n // p][:]
            f.append(p)
            factors.append(f)
            return len(set(f))
    # if len(factors[n]) == 1:
    primes.append(n)
    factors.append([n])
    return 1


def GetNFactors(n, primes, n_pfactors, _):
    """
    using acculumated n_pfactors array
    additionally doing prime-check
    """
    sqrtn = int(n ** 0.5) + 1

    for p in primes:
        if p > sqrtn:
            break
        if n % p == 0:
            n //= p
            if n % p == 0:
                return n_pfactors[n]
            else:
                return n_pfactors[n] + 1

    # n is primes
    primes.append(n)
    return 1


def solve1():
    solve12(GetNFactors)


def solve2():
    solve12(GetNFactors0)


def solve12(getfactor_func):
    primes = [2, 3]
    # number of prime factors
    #         for     1  2  3
    n_pfactors = [0, 0, 1, 1]
    factors = [[], [], [2], [3]]

    n = 4
    while 1:
        n_pfactors.append(getfactor_func(n, primes, n_pfactors, factors))
        #'''
        if n_pfactors[n] == n_pfactors[n - 1] == n_pfactors[n - 2] == n_pfactors[n - 3] == 4:
            print(n - 3, n - 2, n - 1, n)
            [print(e) for e in factors[-4:]]
            break
        n += 1


def main():
    t = time.time()
    solve1()
    print(f"took {time.time()-t} sec")

    t = time.time()
    solve2()
    print(f"took {time.time()-t} sec")


if __name__ == "__main__":
    main()
