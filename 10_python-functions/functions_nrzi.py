# https://ru.hexlet.io/challenges/python_functions_nrzi_exercise/instance
# https://ru.hexlet.io/code_reviews/272810


# Python: Функции → NRZI кодирование

# NRZI код (Non Return to Zero Invertive) — один из способов линейного
# кодирования. Обладает двумя уровнями сигнала и используется для передачи
# битовых последовательностей, содержащих только 0 и 1. NRZI применяется,
# например, в оптических кабелях, где устойчиво распознаются только два
# состояния сигнала — свет и темнота.

# Принцип кодирования
# При передаче логического нуля на вход кодирующего устройства передается
# потенциал, установленный на предыдущем такте (то есть состояние потенциала
# не меняется), а при передаче логической единицы потенциал инвертируется на
# противоположный.

# Реализуйте функцию decode(), которая принимает cтроку в виде графического
# представления линейного сигнала и возвращает строку с бинарным кодом.

def decode(nrzi_code):
    result = []
    just_changed = False

    for c in nrzi_code:
        if c == '|':
            result.append(1)
            just_changed = True
            continue

        if just_changed:
            just_changed = False
        else:
            result.append(0)

    return ''.join(str(c) for c in result)


assert decode('') == ''
assert decode('|¯') == '1'
assert decode('_') == '0'
assert decode('_|¯|____|¯|__|¯¯¯') == '011000110100'
assert decode('|¯|___|¯¯¯¯¯|___|¯|_|¯') == '110010000100111'
assert decode('¯|___|¯¯¯¯¯|___|¯|_|¯') == '010010000100111'
