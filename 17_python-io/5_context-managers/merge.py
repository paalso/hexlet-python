#!/usr/bin/env python3

# https://ru.hexlet.io/courses/python-io/lessons/ /exercise_unit
# https://ru.hexlet.io/code_reviews/1079318

# Python: Основы текстового ввода-вывода -> Менеджеры контекста

# Реализовать функцию merge(file1, file2, out), которая мержит (совмещает)
# два текстовых файла file1 и file2 и записывает результат по указаному пути

def get_discrepancy_record(lines1, lines2):
    discrepancy_records = ['>>>file1>>>\n']
    discrepancy_records.extend(lines1)
    discrepancy_records.append('=====\n')
    discrepancy_records.extend(lines2)
    discrepancy_records.append('<<<file2<<<\n')
    return ''.join(discrepancy_records)


def merge(file1, file2, out):
    not_matched_lines1 = []
    not_matched_lines2 = []
    with open(file1, 'r') as f1, open(file2, 'r') as f2, open(out, 'w') as fout:
        while True:
            line1 = f1.readline()
            line2 = f2.readline()

            if line1 == line2 and not_matched_lines1:
                fout.write(get_discrepancy_record(not_matched_lines1,
                                                  not_matched_lines2))
                not_matched_lines1 = []
                not_matched_lines2 = []

            if line1 == '' or line2 == '':
                return

            if line1 != line2:
                not_matched_lines1.append(line1)
                not_matched_lines2.append(line2)
                continue

            fout.write(line1)


def main():
    merge('file1.txt', 'file2.txt', 'out_from_file1_file2.txt')
    merge('text1.txt', 'text2.txt', 'out_from_text1_text2.txt')
    merge('text1.txt', 'text3.txt', 'out_from_text1_text3.txt')


if __name__ == '__main__':
    main()

'''
# Teacher's version:

def merge(file1, file2, out):
    with (
        open(file1, 'r') as f1,
        open(file2, 'r') as f2,
        open(out, 'w') as fout,
    ):
        diff1 = []
        diff2 = []
        for line1, line2 in zip(f1, f2):
            if line1 == line2:
                if diff1 or diff2:
                    fout.write(make_diff_view(diff1, diff2))
                    diff1 = []
                    diff2 = []
                fout.write(line1)
            else:
                diff1.append(line1)
                diff2.append(line2)
        if diff1 or diff2:
            fout.write(make_diff_view(diff1, diff2))


def make_diff_view(diff1, diff2):
    template = f">>>file1>>>\n{''.join(diff1)}=====\n{''.join(diff2)}<<<file2<<<\n"  # noqa: E501
    return template
'''
