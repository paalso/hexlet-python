#!/usr/bin/env python3

import numpy as np


def main():
    array = np.array([0, 5, 0, 5, 0, 5, 0, 5, 0, 5])
    array_descending_value_ids = np.argsort(-array)
    print(array_descending_value_ids)   # [1 3 7 5 9 2 4 0 6 8]
    filtered_ids = array_descending_value_ids[array[array_descending_value_ids] != 0]
    print(filtered_ids)


if __name__ == '__main__':
    main()
