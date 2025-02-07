# https://ru.hexlet.io/courses/python-polymorphism/lessons/key-dispatch-data/exercise_unit
# https://ru.hexlet.io/code_reviews/1141687

# Python: Полиморфизм
# 4. Диспетчеризация по ключу (функции)

'''
Реализуйте функцию stringify(), которая принимает на вход тег и возвращает
его текстовое представление.
'''


def stringify_attributes(tag):
    TO_EXCLUDE = set(('name', 'tag_type', 'body'))
    attrs_to_stringify = []
    for attr, attr_value in tag.items():
        if attr not in TO_EXCLUDE:
            attrs_to_stringify.append(f' {attr}="{attr_value}"')
    return ''.join(attrs_to_stringify)


mapping = {
    "single": lambda tag: f'<{tag["name"]}{stringify_attributes(tag)}>',
    "pair": lambda tag: f'<{tag["name"]}{stringify_attributes(tag)}>' +
                        f'{tag["body"]}</{tag["name"]}>',
}


def stringify(tag):
    return mapping[tag['tag_type']](tag)


def test_stringify1():
    tag = {
      'name': 'hr',
      'class': 'px-3',
      'id': 'myid',
      'tag_type': 'single',
    }
    html = stringify(tag)

    print(stringify_attributes(tag))
    expected = '<hr class="px-3" id="myid">'
    assert html == expected


def test_stringify2():
    tag = {
      'name': 'p',
      'tag_type': 'pair',
      'body': 'text',
    }
    html = stringify(tag)

    print(stringify_attributes(tag))
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
    print(stringify_attributes(tag))
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


# test_stringify1()
# test_stringify2()
# test_stringify3()


tag1 = {
      'name': 'hr',
      'class': 'px-3',
      'id': 'myid',
      'tag_type': 'single',
    }

tag2 = {
    'name': 'p',
    'tag_type': 'pair',
    'body': 'text',
}

tag3 = {
    'name': 'div',
    'tag_type': 'pair',
    'body': 'text2',
    'id': 'wow',
}

print(stringify(tag3))
