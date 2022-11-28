import math
def luhn_verification(n: str) -> bool:
    r = [int(ch) for ch in str(n)][::-1]
    return (sum(r[0::2]) + sum(sum(divmod(d*2, 10)) for d in r[1::2])) % 10 == 0

def luhn_compute(n: str) -> str:
    r = [int(ch) for ch in str(n)][::-1]
    return 10 - ((sum(r[1::2]) + sum(sum(divmod(d*2, 10)) for d in r[0::2])) % 10)