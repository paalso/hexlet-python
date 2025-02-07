# https://ru.hexlet.io/courses/python-polymorphism/lessons/patterns/exercise_unit
# https://ru.hexlet.io/code_reviews/1163481

# Python: Полиморфизм
# 14. Шаблоны проектирования (Паттерны)

# Реализуйте класс LabelTag, который умеет оборачивать другие теги


from tags.input_tag import InputTag
from tags.label_tag import LabelTag


def save(tag, path):
    html = tag.render()
    with open(path, 'w') as f:
        f.write(html)


def test_tags():
    input_tag = InputTag('submit', 'Save')
    label_tag = LabelTag('Press Submit', input_tag)
    expected = '<label>Press Submit<input type="submit" value="Save"></label>'
    assert label_tag.render() == expected
    assert str(label_tag) == expected


input_tag = InputTag('submit', 'Save')
print(input_tag)

label_tag = LabelTag('Press Submit', input_tag)
print(label_tag.render())
