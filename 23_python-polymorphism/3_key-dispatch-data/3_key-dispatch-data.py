# https://ru.hexlet.io/courses/python-polymorphism/lessons/key-dispatch-data/exercise_unit
# https://ru.hexlet.io/code_reviews/1140130

# Python: Полиморфизм
# 2. Диспетчеризация по ключу

'''
Реализуйте функцию get_links(), которая принимает на вход список тегов,
находит среди них теги a, link и img, а затем извлекает ссылки и возвращает
список ссылок. Теги подаются на вход в виде списка, где каждый элемент это
тег. Тег имеет следующую структуру:
    name — имя тега.
    href или src — атрибуты. Атрибуты зависят от тега: тег img имеет атрибут
    src, тег a — href, link — href.

'''

def get_links(tags):
    TAG_LINK_ATTR_MAPPING = {
        'a': 'href',
        'img': 'src',
        'link': 'href'
    }

    return list(
        filter(bool,
               map(lambda tag: tag.get(TAG_LINK_ATTR_MAPPING.get(tag['name'])),
                   tags)))


def test_get_links_empty():
    tags = []
    links = get_links(tags)

    assert links == []


def test_get_links1():
    tags = [
        {'name': 'p'},
        {'name': 'a', 'href': 'hexlet.io'},
        {'name': 'img', 'src': 'hexlet.io/assets/logo.png'},
    ]

    links = get_links(tags)
    expected = [
      'hexlet.io',
      'hexlet.io/assets/logo.png',
    ]
    print(links)
    assert links == expected


def test_get_links2():
    tags = [
      {'name': 'img', 'src': 'hexlet.io/assets/logo.png'},
      {'name': 'div'},
      {'name': 'link', 'href': 'hexlet.io/assets/style.css'},
      {'name': 'h1'},
    ]
    links = get_links(tags)

    expected = [
      'hexlet.io/assets/logo.png',
      'hexlet.io/assets/style.css',
    ]
    assert links == expected


def test_get_links3():
    tags = [
      {'name': 'invalidTag', 'src': 'hexlet.io/assets/invalid.png'},
      {'name': 'img', 'src': 'hexlet.io/assets/logo.png'},
      {'name': 'div'},
      {'name': 'link', 'href': 'hexlet.io/assets/style.css'},
      {'name': 'h1'},
    ]
    links = get_links(tags)
    expected = [
      'hexlet.io/assets/logo.png',
      'hexlet.io/assets/style.css',
    ]
    assert links == expected


test_get_links_empty()
test_get_links1()

# tags = [
#     { 'name': 'img', 'src': 'hexlet.io/assets/logo.png' },
#     { 'name': 'div' },
#     { 'name': 'link', 'href': 'hexlet.io/assets/style.css' },
#     { 'name': 'h1' },
# ]


# links = get_links(tags)
# print(get_links(tags))

# [
#   'hexlet.io/assets/logo.png',
#   'hexlet.io/assets/style.css'
# ]
