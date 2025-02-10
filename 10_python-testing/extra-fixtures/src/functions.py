from pathlib import Path
import json
import yaml
import os
from dotenv import load_dotenv


parsers_right = {
    "json": json.loads,
    "yaml": yaml.safe_load,
    "csv": lambda data: data.strip().split(',')
}

parsers_wrong1 = {
    "json": lambda data: [],
    "yaml": yaml.safe_load,
    "csv": lambda data: data.strip().split(',')
}

parsers_wrong2 = {
    "json": json.loads,
    "yaml": lambda data: [],
    "csv": lambda data: data.strip().split(',')
}

parsers_wrong3 = {
    "json": json.loads,
    "yaml": yaml.safe_load,
    "csv": lambda data: []
}


def gen_solution(parsers):
    def to_html_list(filepath):
        content = Path(filepath).read_text()
        ext = Path(filepath).suffix[1:]
        items = parsers[ext](content)
        lis = map(lambda item: f"  <li>{item}</li>", items)
        list = "\n".join(lis)
        return f"<ul>\n{list}\n</ul>\n"
    return to_html_list


functions = {
    "right": gen_solution(parsers_right),
    "fail1": gen_solution(parsers_wrong1),
    "fail2": gen_solution(parsers_wrong2),
    "fail3": gen_solution(parsers_wrong3)
}


def get_function():
    load_dotenv()
    name = os.environ['FUNCTION_VERSION']
    return functions[name]
