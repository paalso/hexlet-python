from bs4 import BeautifulSoup


def read(file_path):
    with open(file_path, 'r') as f:
        result = f.read()
    return result


def write(file_path, data):
    with open(file_path, 'w') as f:
        f.write(data)


def prettify_html_file(file_path):
    data = read(file_path)

    write(
        file_path,
        BeautifulSoup(data, 'html.parser').prettify()
    )


def main():
    print(dir(BeautifulSoup))


if __name__ == '__main__':
    main()
