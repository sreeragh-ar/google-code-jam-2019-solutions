import math
import bisect


def get_all_prime_numbers(n):
    # return all prime numbers less than n
    prime_nums = []
    for i in range(2, n+1):
        is_prime = True
        sqrt_i = int(math.sqrt(i))
        for j in range(2, sqrt_i + 1):
            if i % j == 0:
                is_prime = False
                break
        if is_prime:
            prime_nums.append(i)
    return prime_nums


def get_keys(possible_primes, encrypted_text):
    encrypted_text = list(map(int, encrypted_text.split()))
    keys = []
    for index, crypt in enumerate(encrypted_text):
        for prime in possible_primes:
            quotient, remainder = divmod(crypt, prime)
            if remainder == 0:
                keys.append(prime)
                keys.append(quotient)
                break
    return list(set(keys))


n_cases = int(input())
limits = []
lengths = []
encrypted_texts = []
for i in range(n_cases):
    lim_and_length = input().split()
    limits.append(int(lim_and_length[0]))
    lengths.append(int(lim_and_length[1]))
    encrypted_texts.append(input())

all_primes = get_all_prime_numbers(max(limits))
# print(all_primes)


for i in range(n_cases):
    n = limits[i]
    index_of_n = bisect.bisect_right(all_primes, n)
    possible_primes = all_primes[:index_of_n]
    cipher_keys = get_keys(possible_primes, encrypted_texts[i])
    print(cipher_keys)
