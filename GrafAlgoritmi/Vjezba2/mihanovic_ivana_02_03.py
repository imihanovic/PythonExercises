# -*- coding: utf-8 -*-
"""
Napisati funkciju koja u stringu nalazi koliko ima susjednih samoglasnika
"""
def checkNeighbour(string):
    nr=0
    substrings=['ae','ei','io','ou']
    for subs in substrings:
        nr += string.lower().count(subs)
    return nr
print(checkNeighbour("aeibueou"))
print(checkNeighbour("abeibueou"))
print(checkNeighbour("aceaeibueou"))
print(checkNeighbour("aeiou"))