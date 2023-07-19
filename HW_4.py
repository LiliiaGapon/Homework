import math
import time
n = 1000000
def variant_1(n):
    prime = [True] * n
    prime[0], prime[1] = False, False # 0 та 1 не є простими
    for i in range(2, math.ceil(math.sqrt(n))):  # від 2 до квадратного кореня з N
        if prime[i]:  # якщо просте видаляємо всі числа кратні до нього
            j = i * i   # для i=2,j будуть такі значення 4,6,8,10,12... для i=3 j — 9,12,15,18,21...
            while j < n:
                prime[j] = False
                j += i

start = time.time()
primes_th=variant_1(n)
end = time.time()
print(f'Variant_1:', end-start)

def variant_2 (n:int)-> bool:
    for i in range(2,n//2+1):
        if n % i == 0:
            return False
    return True

start = time.time()
primes_th=variant_2(n)
end = time.time()
print(f'Variant_2:', end-start)

def variant_3(n):
    if n == 2 or n == 3:
        return True
    if n % 2 == 0 or n == 1 or n % 3 == 0:
        return False
    for i in range(5, int(n**0.5)+1, 6):
        if n % i == 0 or n % (i + 2) == 0:
            return False
    return True


start = time.time()
primes_simple = [x for x in range(2, n+1) if variant_3(x)]
end = time.time()
print(f'Variant_3:', end-start)

def variant_4(n):
    primes = [2]
    sieve = [True] * (n+1)
    for p in range(3, int(n**0.5)+1, 2):
        if sieve[p]:
            primes.append(p)
            for i in range(p*p, n+1, 2*p):
                sieve[i] = False
    for p in range(int(n**0.5)+1, n+1, 2):
        if sieve[p]:
            primes.append(p)
    return primes

start = time.time()
primes_efficient = variant_4(n)
end = time.time()
print(f'Variant_4:', end-start)