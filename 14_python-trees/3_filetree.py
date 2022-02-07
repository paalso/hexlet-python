# https://ru.hexlet.io/courses/python-trees/lessons/filetree/
#

# Виртуальная файловая система
# =============================
"""
Реализуйте функцию generate, которая создает такую файловую структуру:

python-package  # директория (метаданные: {'hidden': True})
├── Makefile  # файл
├── README.md  # файл
├── dist  # пустая директория
├── tests  # директория
│   └── test_solution.py  # файл
├── pyproject.toml  # файл
└── .venv  # директория (метаданные: {'owner': 'root', 'hidden': False})
    └── lib  # директория
        └── python3.6  # директория
            └── site-packages  # директория
                └── hexlet-python-package.egg-link  # файл

"""
import fs
from fs import mkdir, mkfile


def generate():
	return mkdir(
        'python-package',
        [
            mkfile('Makefile'),
            mkfile('README.md'),
            mkdir('dist', []),
            mkdir('tests', [mkfile('test_solution.py')]),
            mkfile('pyproject.toml'),
            mkdir('.venv', [
                mkdir('lib', [
                    mkdir('python3.6', [
                        mkdir('site-packages', [
                            mkfile('hexlet-python-package.egg-link'),
                        ]),
                    ]),
                ]),
            ], {'owner': 'root', 'hidden': False}),
        ],
        {'hidden': True}
    )


print(generate())
