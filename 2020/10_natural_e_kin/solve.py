from loguru import logger

"""
자연로그 e를 소수로 표현했을 때, 
    연속한 10개의 수가 소수가 되고 
    각 자릿수의 합이 50이 되는 첫번째 소수를 구하시오. 

(예: e=2.71828182845904523536028747135...이므로 
연속한 2개의 수가 소수가 되는 첫번째 경우는 71이고 
자릿수의 합은 8이며, 그 다음은 59이고 각 자릿수의 
합은 14입니다.)
"""

SIPMAN = 100000
SIEV = {i: 1 for i in range(SIPMAN + 1)}
PRIMES = []


def init_primes():
    SIEV[0] = SIEV[1] = 0
    i = 2
    while i * i <= SIPMAN:
        if SIEV[i]:
            ni = 2 * i
            while ni <= SIPMAN:
                SIEV[ni] = 0
                ni += i
        i += 1
    for i in range(SIPMAN):
        if SIEV[i]:
            PRIMES.append(i)


def read_e() -> str:
    with open("natual_e.txt", "rt") as f:
        txt: str = f.read()
        txt = txt.replace("\n", "")
        txt = txt.replace(" ", "")
        return txt
    return ""


def is_prime(n: int) -> bool:
    for p in PRIMES:
        if n % p == 0:
            return False
    return True


def main():
    init_primes()
    e: str = read_e()
    logger.info(f"{e[:100]}")
    e = e.replace(".", "")
    logger.info(f"{e[:100]}")
    for i in range(len(e) - 10):
        n_ = e[i : i + 10]
        digit_sum = sum(map(int, list(n_)))
        if digit_sum == 50:
            n = int(n_)
            if is_prime(n):
                print(n, i, i + 10)
                break


if __name__ == "__main__":
    main()
