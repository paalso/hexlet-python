def bubble_sort(items):
    sorted = False
    size = len(items)
    upper_limit = size - 1
    while not sorted:
        sorted = True
        for i in range(0, upper_limit):
            if items[i + 1] < items[i]:
                items[i + 1], items[i] = items[i], items[i + 1]
                sorted = False
        upper_limit -= 1


def bubble_sort_hexlet(items):
    for limit in range(len(items) - 1, 0, -1):
        for i in range(limit):
            if items[i] > items[i + 1]:
                items[i], items[i + 1] = items[i + 1], items[i]


def selection_sort(items):
    size = len(items)
    for i in range(size - 1):
        current = items[i]
        min_id = i
        for j in range(i, size):
            if items[j] < current:
                min_id = j
        items[i], items[min_id] = items[min_id], items[i]


def quick_sort(items):
    _quick_sort_subarray(items, 0, len(items) - 1)


def _partition(items, left_id, right_id, pivot):
    '''
    разбить массив на две части таким оборазом,
    чтобы все в левой части были не больше опорного
    и не больше всех элементов в правой части
    '''
    while True:
        # ищем какую-нибудь пару, для которой левый элемент больше опорного,
        # а правый элемент меньше опроного
        while items[left_id] < pivot:
            left_id += 1
        while items[right_id] > pivot:
            right_id -= 1

        if left_id >= right_id:
            return right_id + 1
        
        items[left_id], items[right_id] = items[right_id], items[left_id]
        left_id += 1
        right_id -= 1


def _quick_sort_subarray(items, left_id, right_id):
    if right_id - left_id < 1:
        return        

    pivot = items[left_id]
    separating_id = _partition(items, left_id, right_id, pivot)

    _quick_sort_subarray(items, left_id, separating_id - 1)
    _quick_sort_subarray(items, separating_id, right_id)
