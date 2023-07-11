# https://ru.hexlet.io/courses/python-io/lessons/line-by-line/exercise_unit
# https://ru.hexlet.io/code_reviews/1077698

# Python: Основы текстового ввода-вывода -> Построчные чтение и запись

# Реализуйте функцию transform(input_file, output_file, rules), которая
# принимает на вход путь до текстового файла, путь по которому нужно
# записать результат и обрабатывает текст согласно словарю rules
# следующим образом:

# word_min_len    - отфильтровывает слова меньше минимальной длины
# censored_words  - список слов, которые нужно удалить из текста
# capital_letters - список букв, которые нужно привести к заглавным,
#                     если слово на них начинается

def capitalize_word(word, letters_to_capitalize):
    for letter in letters_to_capitalize:
        if word.startswith(letter):
            return word.capitalize()
    return word


def filter_out_short_words(words, word_min_len):
    return filter(lambda word: len(word) >= word_min_len, words)


def filter_out_censored_words(words, censored_words):
    return filter(lambda word: word not in censored_words, words)


def capitalize_for_special_letters(words, letters_to_capitalize):
    return map(
        lambda word: capitalize_word(word, letters_to_capitalize), words)


def process_line(line, rules):
    words = line.split()

    words_without_short = filter_out_short_words(
        words, rules['word_min_len'])

    words_without_censored = filter_out_censored_words(
        words_without_short, rules['censored_words'])

    result_words = capitalize_for_special_letters(
        words_without_censored, rules['capital_letters'])

    return ' '.join(result_words) + '\n'


def transform(input_file, output_file, rules):
    f_in = open(input_file, 'r')
    f_out = open(output_file, 'w')
    for line in f_in:
        processed_line = process_line(line, rules)
        if processed_line.rstrip('\n') == '':
            continue
        f_out.write(processed_line)


RULES1 = {
    'word_min_len': 3,
    'censored_words': ['better', 'pass'],
    'capital_letters': ['n', 'c'],
}

RULES2 = {
    'word_min_len': 5,
    'censored_words': ['explain', 'implementation'],
    'capital_letters': ['s', 'p'],
}

rules = RULES2

transform('python.txt', 'out.txt', rules=rules)
print(open('out.txt').read())
