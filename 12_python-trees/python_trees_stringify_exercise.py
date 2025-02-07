# https://ru.hexlet.io/challenges/python_trees_stringify_exercise
# https://ru.hexlet.io/code_reviews/460386

# Python: JSON stringify
# =======================

"""
JavaScript содержит метод JSON.stringify() для приведения к строке любого
значения. Он работает следующим образом:

JSON.stringify('hello'); // "hello" - для строковых значений добавляются кавычки
JSON.stringify(true);    // true    - значение приведено к строке, без кавычек
JSON.stringify(5);       // 5

const data = { hello: 'world', is: true, nested: { count: 5 } };
JSON.stringify(data); // {"hello":"world","is":true,"nested":{"count":5}}

JSON.stringify(data, null, 2); // null, 2 - указывают на два пробела перед ключом
// ключам добавляются кавычки
// в конце каждой строчки (линии) добавляется запятая, если имеется значение ниже
// {
//   "hello": "world",
//   "is": true,
//   "nested": {
//     "count": 5
//   }
// }


Реализуйте функцию stringify(), похожую на JSON.stringify(),
но со следующими отличиями:

ключи и строковые значения должны быть без кавычек;
строчка (линия) в строке заканчивается самим значением, без запятой.
Синтаксис:

stringify(value[, replacer[, spaces_count]])
Параметры:

-- value
            Значение, преобразуемое в строку.
-- replacer, необязательный
            Строка – отступ для ключа; Значение по умолчанию – один пробел.
-- spacesCount, необязательный
            Число – количество повторов отступа ключа. По умолчанию – 1
"""


def stringify(data, replacer=" ", spacesCount=1):

    def helper(data, depth):
        if type(data) in (str, bool, int):
            return str(data)

        inner_tokens = ("{}{}: {}".format(
            replacer * (depth * spacesCount), key, helper(value, depth + 1))
            for key, value in data.items())
        tokens = ["{", *inner_tokens,
            "{}".format(replacer * ((depth - 1) * spacesCount)) + "}"]
        return "\n".join(tokens)

    return helper(data, 1)


assert stringify('hello') == "hello"  # значение приведено к строке, но не имеет кавычек
assert stringify(True) is "True"
assert stringify(5) == "5"

data = { "hello": "world", "is": True, "nested": { "count": 5 } }
print(stringify(data, '-', 3))

print()
data = {"a":1}
print(stringify(data))

# Author's Version
# BEGIN
def stringify(value, replacer=' ', spaces_count=1):

    def iter_(current_value, depth):
        if not isinstance(current_value, dict):
            return str(current_value)

        deep_indent_size = depth + spaces_count
        deep_indent = replacer * deep_indent_size
        current_indent = replacer * depth
        lines = []
        for key, val in current_value.items():
            lines.append(f'{deep_indent}{key}: {iter_(val, deep_indent_size)}')
        result = itertools.chain("{", lines, [current_indent + "}"])
        return '\n'.join(result)

    return iter_(value, 0)
# END
