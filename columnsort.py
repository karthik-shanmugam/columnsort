from __future__ import print_function
from random import shuffle

def columnsort(data, r, s):
    def display(columns):
        for column in columns:
            print(column)
        print()

    def sort_stage(columns):
        for column in columns:
            column.sort()

    assert r*s <= len(data), "input list too small"
    assert r >= 2*((s-1)*(s-1)), "s is too large"
    #data = data[:r*s]
    columns = [data[i*r:(i+1)*r] for i in range(s)]
    print("input:")
    display(columns)
    sort_stage(columns)
    print("after step 1:")
    display(columns)


if __name__ == "__main__":
    data = list(range(30))
    shuffle(data)
    columnsort(data, 10, 3)