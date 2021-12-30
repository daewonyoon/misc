# Author : DwYoon
# PROJECT EULER
# http://projecteuler.net/index.php?section=problems&id=47
# PROBLEM 47
import time


def GetNFactors0(n, primes, _):
    """
    stupid
    """
    m = n
    i = 0
    l = len(primes)
    factors = []
    while i < l - 1:
        p = primes[i]
        if m % p == 0:
            if p not in factors:
                factors.append(p)
            m //= p
            i -= 1
        i += 1

    if len(factors) == 0:
        primes.append(m)
        return 1
    return len(factors)


def GetNFactors(n, primes, n_pfactors):
    """
    using acculumated n_pfactors array
    additionally doing prime-check
    """
    sqrtn = int(n**.5) + 1

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
    n_pfactors = [0, 0, 1, 2]

    n = 4
    while 1:
        n_pfactors.append(getfactor_func(n, primes, n_pfactors))
        #'''
        if n_pfactors[n] == 4 and n_pfactors[n - 1] == 4 and n_pfactors[n - 2] == 4 and n_pfactors[n - 3] == 4:
            print(n - 3, n - 2, n - 1, n)
            break
        """     
        if n_pfactors[n] == 3 and n_pfactors[n-1] == 3 and n_pfactors[n-2] == 3:         
            print (n-2, n-1, n)
            break     
        """
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
