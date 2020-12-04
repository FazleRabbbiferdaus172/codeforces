import sys
input = sys.stdin.readline


def list_input():
    return list(map(int, input().split()))


def float_compare(a, b):
    if abs(a-b) < float(1e-9):
        return True
    else:
        return False


def sub_mod(x, mod):
    x = x % mod
    if x < 0:
        x += mod
    return x


def divisor(n):
    i = 1
    dv = []
    while i*i <= n:
        if n % i == 0:
            dv.append(i)
            if i*i != n:
                dv.append(n//i)
        i += 1

    return dv


def binpow(a, n):
    ans = 1
    # MOD =
    while n:
        if n & 1:
            ans *= a
            #ans =  (ans * a) % MOD
        a *= a
        #a = (a*a) % MOD
        n >>= 1
    return ans


for _ in range(int(input().strip())):
    n, m = map(int, input().split())
    l_n = list_input()
    l_m = list_input()
    cou = 0
    if n >= m:
        for i in l_m:
            if i in l_n:
                cou += 1
    else:
        for i in l_n:
            if i in l_m:
                cou += 1

    print(cou)
