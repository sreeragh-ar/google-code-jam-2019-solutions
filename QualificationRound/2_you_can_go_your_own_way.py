# Solution for problem
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

n_cases = int(input())
lydia_paths = []


def get_new_path(explored_path):
    new_path = explored_path.replace(
        'S', 'X').replace('E', 'S').replace('X', 'E')
    return new_path


for i in range(n_cases):
    input()  # size is not used
    lydia_paths.append(input())

for i in range(n_cases):
    print('Case #{}: {}'.format(i+1, get_new_path(lydia_paths[i])))
