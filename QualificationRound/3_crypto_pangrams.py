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


def factorise(keys, keys_product):
    for prime in keys:
        quotient, remainder = divmod(keys_product, prime)
        if remainder == 0:
            return prime, quotient


def get_keys(possible_primes, encrypted_text):
    keys = []
    for index, crypt in enumerate(encrypted_text):
        keys += factorise(possible_primes, crypt)
    return list(set(keys))


def get_key_sequence(encrypted_text, cipher_keys):
    text_len = len(encrypted_text)
    key_sequence = []
    for i in range(text_len - 1):
        current_keys = factorise(cipher_keys, encrypted_text[i])
        next_keys = factorise(cipher_keys, encrypted_text[i+1])
        if (current_keys[0] == next_keys[0]) or (current_keys[0] == next_keys[1]):
            key_sequence.append(current_keys[0])
        else:
            key_sequence.append(current_keys[1])
    first_key = [encrypted_text[0]//key_sequence[0]]
    last_key = [encrypted_text[-1]//key_sequence[-1]]
    key_sequence = first_key + key_sequence + last_key
    print(key_sequence)


def get_decrypt_dict(cipher_keys):
    decrypt_dict = {}
    ascii_start = 65
    for i, key in enumerate(cipher_keys):
        decrypt_dict[key] = chr(ascii_start + i)
    return decrypt_dict


n_cases = int(input())
limits = []
lengths = []
encrypted_texts = []
for i in range(n_cases):
    lim_and_length = input().split()
    limits.append(int(lim_and_length[0]))
    lengths.append(int(lim_and_length[1]))
    encrypted_text = input()
    encrypted_text = list(map(int, encrypted_text.split()))
    encrypted_texts.append(encrypted_text)

all_primes = get_all_prime_numbers(max(limits))
# print(all_primes)


for i in range(n_cases):
    n = limits[i]
    index_of_n = bisect.bisect_right(all_primes, n)
    possible_primes = all_primes[:index_of_n]
    cipher_keys = get_keys(possible_primes, encrypted_texts[i])
    decrypt_dict = get_decrypt_dict(cipher_keys)
    print(decrypt_dict)
    print(cipher_keys)
    key_sequence = get_key_sequence(encrypted_texts[i], cipher_keys)
    # decrypted_text = get_decrypted_text(key_sequence)
    # print("DECRYPTED\n", decrypted_text)
