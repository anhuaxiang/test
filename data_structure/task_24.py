import itertools


def combinationSum(candidates=[2, 3, 6, 7], target=7):
    a = []
    r = []
    repeat = target // min(candidates)
    for i in range(1, repeat + 1):
        a += list(itertools.product(candidates, repeat=i))
    for i in a:
        b = list(i)
        b.sort()
        if sum(b) == target and b not in r:
            r.append(b)
    return r


if __name__ == '__main__':
    print(combinationSum(candidates=[5, 10, 8, 4, 3, 12, 9], target=27))
    import pandas as pd

    pd.read_csv()
    pd.read_excel()