# https://ru.hexlet.io/courses/python-polymorphism/lessons/key-dispatch-data/exercise_unit
# https://ru.hexlet.io/code_reviews/1141687

# Python: Полиморфизм
# 4. Диспетчеризация по ключу (функции)

'''
Реализуйте функцию stringify(), которая принимает на вход тег и возвращает
его текстовое представление.
'''


def stringify_attribute(tag, attribute=None):
    attribute_value = tag.get(attribute)
    return f'{attribute}="{attribute_value}"' if attribute_value else ''


def clear_items(items, items_to_exclude):
    return filter(lambda e: e not in items_to_exclude, items)


def stringify(tag):
    attributes = clear_items(tag.keys(), ('name', 'tag_type', 'body'))
    attribute_tokens = filter(bool, map(
        lambda attr: stringify_attribute(tag, attr), attributes))
    tag_name = tag['name']
    stringified_attributes = ' '.join(attribute_tokens)
    separator = ' ' if stringified_attributes else ''
    stringified_tag = f"<{tag_name}{separator}{stringified_attributes}>"
    if tag['tag_type'] == 'single':
        return stringified_tag
    body = tag['body']
    return f'{stringified_tag}{body}</{tag_name}>'


def test_stringify1():
    tag = {
      'name': 'hr',
      'class': 'px-3',
      'id': 'myid',
      'tag_type': 'single',
    }
    html = stringify(tag)

    expected = '<hr class="px-3" id="myid">'
    assert html == expected


def test_stringify2():
    tag = {
      'name': 'p',
      'tag_type': 'pair',
      'body': 'text',
    }
    html = stringify(tag)

    expected = '<p>text</p>'
    print(html)
    assert html == expected


def test_stringify3():
    tag = {
      'name': 'div',
      'tag_type': 'pair',
      'body': 'text2',
      'id': 'wow',
    }
    html = stringify(tag)
    expected = '<div id="wow">text2</div>'
    assert html == expected


def test_stringify4():
    fake = Faker()
    random_attr = fake.word()
    tag = {
      'name': 'div',
      'tag_type': 'pair',
      'body': 'text2',
      'id': 'wow',
      random_attr: 'value',
    }
    html = stringify(tag)

    expected = f'<div id="wow" {random_attr}="value">text2</div>'
    assert html == expected


test_stringify1()
test_stringify2()
test_stringify3()


'''
hr_tag = {
  'name': 'hr',
  'class': 'px-3',
  'id': 'myid',
  'tag_type': 'single',
}
html = stringify(hr_tag)    # <hr class="px-3" id="myid">
print(html)

div_tag = {
  'name': 'div',
  'tag_type': 'pair',
  'body': 'text2',
  'id': 'wow',
}
html = stringify(div_tag)   # <div id="wow">text2</div>
print(html)

empty_div_tag = {
  'name': 'div',
  'tag_type': 'pair',
  'body': '',
  'id': 'empty',
}
html = stringify(empty_div_tag)     # <div id="empty"></div>
print(html)
'''
