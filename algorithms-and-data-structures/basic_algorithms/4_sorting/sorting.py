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




def partition(items, left, right, pivot):
    '''
    разбить массив на две части таким оборазом,
    чтобы все в левой части были не больше опорного
    и не больше всех элементов в правой части
    '''
    while True:
        # ищем какую-нибудь пару, для которой левый элемент больше опроного,
        # а правый элемент меньше опроного
        pass

def sort_subarray(items, left, right):
    pass
