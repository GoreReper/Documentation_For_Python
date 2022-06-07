map = {"i": 0, 1986: {"i": 2, 2015: {
    "i": 4, 2014: {"i": 3, "C": 0, "LOGOS": 1, "ADA": 2},
    2018: {"i": 1, "PERL6": 3, "HY": 4, "BISON": 5},
    1972: {"i": 3, "C": 6, "LOGOS": 7, "ADA": 8}}, 2007: 9},
    1970: 10, 2010: 11}


def main(arr):
    current = map[arr[0]]
    while type(current) != int:
        current = current[arr[current["i"]]]
    return current
