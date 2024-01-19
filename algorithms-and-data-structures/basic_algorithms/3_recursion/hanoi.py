#!/usr/bin/env python3


def hanoi(height, from_stake, to_stake):
    if height == 1:
        print(f'from {from_stake} to {to_stake}')
        return
    temp_stake = 6 - from_stake - to_stake
    hanoi(height - 1, from_stake, temp_stake)
    print(f'from {from_stake} to {to_stake}')
    hanoi(height - 1, temp_stake, to_stake)


def main():
    hanoi(20, 1, 3)


if __name__ == '__main__':
    main()
