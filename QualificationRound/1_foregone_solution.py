# Solution for problem
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/0000000000088231

n_cases = int(input())
samples = []
for i in range(n_cases):
    samples.append(input())

samples = samples[:n_cases]

for i, sample in enumerate(samples):
    str1 = ''
    str2 = ''
    for ch in sample:
        if ch != '4':
            str1 += ch
            str2 += '0'
        else:
            str1 += '2'
            str2 += '2'
    print('Case #{}: {} {}'.format(i+1, str1, str2))
