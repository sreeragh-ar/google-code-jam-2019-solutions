# Solution for problem
# https://codingcompetitions.withgoogle.com/codejam/round/0000000000051705/00000000000881da

n_cases = int(input())
sizes = []
lydia_paths = []


def get_new_path(size, explored_path):
    steps_in_a_dir = size - 1
    total_steps = steps_in_a_dir * 2
    total_steps = len(explored_path)
    new_path = ''
    for i in range(total_steps):
        if explored_path[i] == 'S':
            new_path += 'E'
        else:
            new_path += 'S'
    return new_path


for i in range(n_cases):
    sizes.append(int(input()))
    lydia_paths.append(input())

for i in range(n_cases):
    print('Case #{}: {}'.format(i+1, get_new_path(sizes[i], lydia_paths[i])))
