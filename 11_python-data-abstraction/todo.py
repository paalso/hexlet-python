#!/usr/bin/env python3

# https://ru.hexlet.io/challenges/python_data_abstraction_todo_exercise/instance
# 

# Python: Абстракция с помощью данных
# Испытание: Список дел

"""
Реализуйте абстракцию для работы со списком дел с тегами.

Cущность Задача (task) должна быть представлена словарем со следующими ключами:

    description - описание задачи (строка)
    completed - статус задачи (выполнена или нет, булево значение)
    tags - список строк, связанных с этой задачей

Необходимо реализовать следующую функциональность:

    create_task(description, tags) - создаёт и возвращает новый словарь задачи с заданными описанием и тегами. Убедитесь, что в созданной задаче в поле tags нет дубликатов.
    add_task(tasks, task) - добавляет задачу в глобальный список tasks и возвращает список задач.
    add_tag_to_task(tasks, task_id, tag) - добавляет тег к задаче, если его там ещё нет, и возвращает список задач.
    remove_tag_from_task(tasks, task_id, tag) - удаляет тег у задачи, и возвращает список задач
    mark_task_completed(tasks, task_id) - помечает задачу как выполненную, и возвращает спиок задач
    filter_tasks_by_tags(tasks, filter_tags) - получает список тегов и возвращает новый список, содержащий только задачи, у которых есть все указанные теги. Если filter_tags не указан, то возвращается список всех задач.

"""
from pprint import pprint
from uuid import uuid4


# BEGIN (write your solution here)
def create_task(description, tags):
    return {
        'id': int(uuid4()),
        'description': description,
        'completed': False,
        'tags': list(set(tags))
    }

def add_task(tasks, task):
    tasks.append(task)
    return tasks


def add_tag_to_task(tasks, task_id, tag):
    task = _get_task_by_id(tasks, task_id)
    if task:
        task_tags = task['tags']
        if tag not in task_tags:
            task_tags.append(tag)
    return tasks


def remove_tag_from_task(tasks, task_id, tag):
    task = _get_task_by_id(tasks, task_id)
    if task:
        task_tags = task['tags']
        if tag in task_tags:
            task_tags.remove(tag)
    return tasks


def mark_task_completed(tasks, task_id):
    task = _get_task_by_id(tasks, task_id)
    if task:
        task['completed'] = True
    return tasks


def filter_tasks_by_tags(tasks, filter_tags=[]):
    return \
        list(
            filter(
                lambda task: set(filter_tags).issubset(set(task['tags'])),
                tasks
            )
        )


def _get_task_by_id(tasks, id_):
    for task in tasks:
        if task['id'] == id_:
            return task


def main():
    tasks = []
    task1 = create_task('Task 1', ['tag1', 'tag2', 'tag2'])
    id_ = task1['id']
    pprint(task1)

    pprint(add_task(tasks, task1))

    add_tag_to_task(tasks, id_, 'tag3')
    pprint(tasks)

    add_tag_to_task(tasks, id_, 'tag2')
    pprint(tasks)

    remove_tag_from_task(tasks, id_, 'tag1')
    pprint(tasks)

    remove_tag_from_task(tasks, id_, 'tag1')
    pprint(tasks)

    pprint(filter_tasks_by_tags(tasks, ['tag2']))


def tests():
    pass

if __name__ == '__main__':
    main()
