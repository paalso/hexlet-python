# https://ru.hexlet.io/challenges/python_lists_summary_ranges_exercise
# https://ru.hexlet.io/code_reviews/214092

# Python: Список диапазонов
# ==========================
# Реализуйте функцию summary_ranges, которая находит в списке непрерывные
# возрастающие последовательности чисел и возвращает список с их перечислением.

def summary_ranges(items):
    if not items:
        return []

    result = []
    inside = False
    items.append(items[-1])

    for i in range(1, len(items)):
        if items[i] - items[i - 1] == 1:
            if inside == False:
                first = items[i - 1]
            inside = True
        else:
            if inside == True:
                result.append("{}->{}".format(first, items[i - 1]))
            inside = False

    items.pop()
    return result


assert summary_ranges([]) == []
assert summary_ranges([1]) == []
assert summary_ranges([1, 2, 3]) ==  ['1->3']
assert summary_ranges([0, 1, 2, 4, 5, 7]) ==  ['0->2', '4->5']
assert summary_ranges([110, 111, 112, 111, -5, -4, -2, -3, -4, -5]) == \
                        ['110->112', '-5->-4']



def summary_ranges1(numbers):
    if not numbers:
        return []

    ranges = []
    current_sequence = [numbers[0]]
    sequences = [current_sequence]

    for x, y in zip(numbers, numbers[1:]):
        if (y - x) == 1:
            current_sequence.append(y)
        else:
            current_sequence = [y]
            sequences.append(current_sequence)

    # здесь [0, 1, 2, 7, 5, 6] уже преобразован
    # в [[0, 1, 2], [7], [5, 6]]

    for sequence in sequences:
        if len(sequence) > 1:
            first, last = sequence[0], sequence[-1]
            ranges.append('{}->{}'.format(first, last))

    return ranges


# === Benchmarking =======================================================

def generate_random_int_array(size, min_, max_):
    import random
    return [random.randint(min_, max_) for _ in range(size)]


L = generate_random_int_array(1000, 1, 10)
print(L[:20])


def get_duration(func, *args, N=10000):
    import time
    start_time = time.time()
    for _ in range(N):
        func(*args)
    return time.time() - start_time


print(get_duration(summary_ranges, L))
result = summary_ranges(L)
print(result)
print()
print(get_duration(summary_ranges1, L))
result = summary_ranges1(L)
print(result)
