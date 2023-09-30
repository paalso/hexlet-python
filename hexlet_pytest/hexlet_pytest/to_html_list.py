import os
import json
import yaml


parsers = {
    "json": json.loads,
    "yaml": yaml.safe_load,
    "csv": lambda data: data.strip().split(',')
}


def to_html_list(filepath):
    f = open(filepath)
    content = f.read()
    ext = os.path.splitext(filepath)[1][1:]
    items = parsers[ext](content)
    lis = map(lambda item: f"  <li>{item}</li>", items)
    list = "\n".join(lis)
    return f"<ul>\n{list}\n</ul>"


def main():
    filepath = 'tests/fixtures/list.yaml'
    print(to_html_list(filepath))


if __name__ == '__main__':
    main()
