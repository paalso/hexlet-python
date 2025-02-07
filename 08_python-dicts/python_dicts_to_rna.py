# https://ru.hexlet.io/challenges/python_dicts_to_rna

# Python: Преобразование DNA в RNA
# =================================

# Напишите функцию to_rna, которая принимает на вход цепь ДНК и возвращает
# соответствующую цепь РНК (совершает транскрипцию РНК).
# Цепь РНК составляется на основе цепи ДНК последовательной заменой каждого
# нуклеотида:
# G -> C
# C -> G
# T -> A
# A -> U


def to_rna(dna_sequence):
    dna_to_rna_dict = {"G": "C", "C": "G", "T": "A", "A": "U"}
    return  "".join(dna_to_rna_dict[dna] for dna in dna_sequence)


assert to_rna('ACGTGGTCTTAA') == 'UGCACCAGAAUU'

# def to_rna(nucleotide):
#     dna_to_rna_dict = {"G": "C", "C": "G", "T": "A", "A": "U"}
#     return ''.join(map(dna_to_rna_dict.get, nucleotide))
