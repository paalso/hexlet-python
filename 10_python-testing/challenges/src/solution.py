def custom_sort(coll, reverse=False):
    """Reverse string

    >>> custom_sort([])
    []

    >>> custom_sort([3, 1, 2, 1])
    [1, 1, 2, 3]

    >>> custom_sort([3, 1, 2, 1], reverse=True)
    [3, 2, 1, 1]
    """
    limit = len(coll) - 1
    sorted = False
    while not sorted:
        sorted = True
        for i in range(limit):
            if coll[i + 1] < coll[i]:
                sorted = False
                coll[i + 1], coll[i] = coll[i], coll[i + 1]
        limit -= 1
    if reverse:
        coll.reverse()
    return coll


if __name__ == "__main__":
    import doctest
    doctest.testmod()
