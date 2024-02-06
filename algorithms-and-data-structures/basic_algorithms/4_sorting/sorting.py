def bubble_sort(items):
    sorted = False
    size = len(items)
    upper_limit = size - 1
    while not sorted:
        sorted = True
        for i in range(0, upper_limit):
            if items[i + 1] < items[i]:
                _swap(items, i, i + 1)
                sorted = False
        upper_limit -= 1


def bubble_sort_hexlet(items):
    for limit in range(len(items) - 1, 0, -1):
        for i in range(limit):
            if items[i] > items[i + 1]:
                    _swap(items, i, i + 1)


def selection_sort(items):
    size = len(items)
    for i in range(size - 1):
        current_min = items[i]
        min_id = i
        for j in range(i + 1, size):
            if items[j] < current_min:
                min_id = j
                current_min = items[min_id]
        _swap(items, i, min_id)


def insertion_sort(items):
    size = len(items)
    for i in range(1, size):
        value = items[i]
        j = i - 1
        while value < items[j] and j >= 0:
            _swap(items, j, j + 1)
            j -= 1


def quick_sort(items):
    _quick_sort_subarray(items, 0, len(items) - 1)


def quick_sort3(items):
    _quick_sort3_subarray(items, 0, len(items) - 1)


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
        
        _swap(items, left_id, right_id)
        left_id += 1
        right_id -= 1


def _quick_sort_subarray(items, left_id, right_id):
    if right_id - left_id < 1:
        return        

    pivot = items[left_id]
    separating_id = _partition(items, left_id, right_id, pivot)

    _quick_sort_subarray(items, left_id, separating_id - 1)
    _quick_sort_subarray(items, separating_id, right_id)


def _quick_sort3_subarray(items, left, right):
    if right - left < 1:
        return
    
    pivot = items[(left + right) // 2]

    equals_left_id, equals_rigth_id = _get_partition3(items, left, right, pivot)
    _quick_sort3_subarray(items, left, equals_left_id - 1)
    _quick_sort3_subarray(items, equals_rigth_id + 1, right)


def _get_partition3(items, left, right, pivot):
    lt = i = left
    gt = right
    while i <= gt:
        if items[i] < pivot:
            _swap(items, i, lt)
            i += 1
            lt += 1
        elif items[i] > pivot:
            _swap(items, i, gt)
            gt -= 1
        else:
            i += 1
    return lt, gt


def _swap(items, i, j):
    items[i], items[j] = items[j], items[i]
