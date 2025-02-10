from functions import get_function


def main():
    func = get_function()
    print(func)
    print(func.__name__)


if __name__ == '__main__':
    main()
