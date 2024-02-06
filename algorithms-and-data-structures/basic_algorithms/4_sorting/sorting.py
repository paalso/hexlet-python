def bubble_sort(array):
    sorted = False
    size = len(array)
    upper_limit = size - 1
    while not sorted:
        sorted = True
        for i in range(0, upper_limit):
            if array[i + 1] < array[i]:
                _swap(array, i, i + 1)
                sorted = False
        upper_limit -= 1


def bubble_sort_hexlet(array):
    for limit in range(len(array) - 1, 0, -1):
        for i in range(limit):
            if array[i] > array[i + 1]:
                    _swap(array, i, i + 1)


def selection_sort(array):
    size = len(array)
    for i in range(size - 1):
        current_min = array[i]
        min_id = i
        for j in range(i + 1, size):
            if array[j] < current_min:
                min_id = j
                current_min = array[min_id]
        _swap(array, i, min_id)


def insertion_sort(array):
    size = len(array)
    for i in range(1, size):
        value = array[i]
        j = i - 1
        while value < array[j] and j >= 0:
            _swap(array, j, j + 1)
            j -= 1


def merge_sort(array):
    size = len(array)
    if size < 2:
        return
    mid_id = size // 2
    left_subarray = array[:mid_id]
    right_subarray = array[mid_id:]
    merge_sort(left_subarray)
    merge_sort(right_subarray)
    temp_array = _merge(left_subarray, right_subarray)
    for i in range(size):
        array[i] = temp_array[i]


def quick_sort(array):
    _quick_sort_subarray(array, 0, len(array) - 1)


def quick_sort3(array):
    _quick_sort3_subarray(array, 0, len(array) - 1)


def _partition(array, left_id, right_id, pivot):
    '''
    разбить массив на две части таким оборазом,
    чтобы все в левой части были не больше опорного
    и не больше всех элементов в правой части
    '''
    while True:
        # ищем какую-нибудь пару, для которой левый элемент больше опорного,
        # а правый элемент меньше опроного
        while array[left_id] < pivot:
            left_id += 1
        while array[right_id] > pivot:
            right_id -= 1

        if left_id >= right_id:
            return right_id + 1
        
        _swap(array, left_id, right_id)
        left_id += 1
        right_id -= 1


def _quick_sort_subarray(array, left_id, right_id):
    if right_id - left_id < 1:
        return        

    pivot = array[left_id]
    separating_id = _partition(array, left_id, right_id, pivot)

    _quick_sort_subarray(array, left_id, separating_id - 1)
    _quick_sort_subarray(array, separating_id, right_id)


def _quick_sort3_subarray(array, left, right):
    if right - left < 1:
        return
    
    pivot = array[(left + right) // 2]

    equals_left_id, equals_rigth_id = _get_partition3(array, left, right, pivot)
    _quick_sort3_subarray(array, left, equals_left_id - 1)
    _quick_sort3_subarray(array, equals_rigth_id + 1, right)


def _get_partition3(array, left, right, pivot):
    lt = i = left
    gt = right
    while i <= gt:
        if array[i] < pivot:
            _swap(array, i, lt)
            i += 1
            lt += 1
        elif array[i] > pivot:
            _swap(array, i, gt)
            gt -= 1
        else:
            i += 1
    return lt, gt


def _swap(array, i, j):
    array[i], array[j] = array[j], array[i]


def _merge(array1, array2):
    i = j = 0
    size1 = len(array1)
    size2 = len(array2)
    result = []

    while i < size1 and j < size2:
        if array1[i] < array2[j]:
            result.append(array1[i])
            i += 1
        else:
            result.append(array2[j])
            j += 1

    result.extend(array1[i:])
    result.extend(array2[j:])

    return result
