#!/usr/bin/env python3

from mobile_screen import MobileScreen


def main():
    ms = MobileScreen()
    print(ms)
    ms.touch()
    ms.swipe()

    ms.set_state('screen_on')
    print(ms)
    ms.touch()
    ms.swipe()

    ms.set_state('screen_disabled')
    print(ms)
    ms.touch()
    print(ms)
    ms.swipe()

    ms.set_state('screen_disabled')
    print(ms)
    ms.swipe()
    ms.touch()


if __name__ == '__main__':
    main()
