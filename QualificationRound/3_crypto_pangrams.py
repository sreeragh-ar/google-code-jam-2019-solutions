import math


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
print(all_primes)
