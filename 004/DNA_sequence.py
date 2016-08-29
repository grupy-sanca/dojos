"""
Problem: Complementary DNA

This problem was taken from codewars, you can check it here:
    https://www.codewars.com/kata/complementary-dna
"""


def DNA_strand_v1(dna):
    # Solution first version
    dna2 = []
    for i in dna:
        if i == 'A':
            dna2.append('T')
        elif i == 'T':
            dna2.append('A')
        elif i == 'C':
            dna2.append('G')
        elif i == 'G':
            dna2.append('C')
    return ''.join(dna2)


def DNA_strand_v2(dna):
    # Solution second version
    dna2 = []
    dict_dna2 = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    for i in dna:
        dna2.append(dict_dna2[i])
    return ''.join(dna2)


def DNA_strand(dna):
    # Last solution (second version refactored)
    dict_dna2 = {'A': 'T', 'T': 'A', 'C': 'G', 'G': 'C'}
    return ''.join(dict_dna2[i] for i in dna)
