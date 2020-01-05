#!/usr/bin/python3
from random import choice
import os
import operator

FILENAME = "values1.txt"

values = {}


def clear(text=""):
    # for linux and mac
    if os.name == "posix":
        _ = os.system("clear")

    # for windows (here, os.name is 'nt')
    else:
        _ = os.system("cls")

    if text:
        print(text)


def main():
    with open(FILENAME, "r") as f:
        for v in f:
            values[v[:-1]] = 0

    def get_input() -> int:
        """ Returns a number, if one got 'inputted'.
        Might throw a KeyboardInterrupt.

        Args:
            None

        Returns:
            int: number between 1 and 3

        Throws:
            KeyboardInterrupt, if the user intends to end inputting values
        """
        try:
            inp = input()
        except EOFError:
            raise KeyboardInterrupt("exiting")

        lower = inp.lower()
        if lower == "exit" or lower == "end" or not lower:
            raise KeyboardInterrupt("exiting")

        try:
            index = int(inp)
            assert index > 0
            assert index < 4
        except (ValueError, AssertionError):
            print("Please enter '1', '2' or '3' to select one of the presented values")
            return get_input()  # this might lead to a very unlikely
            # 'recursion limit error' when repeated more than 5k times.
        return index

    for _ in range(2 ** len(values)):
        selection = [choice([*values]), choice([*values]), choice([*values])]
        clear()
        print("{0} {1} {2}".format(selection[0], selection[1], selection[2]))

        try:
            index = get_input()
            values[selection[index - 1]] += 1
        except KeyboardInterrupt as e:
            break

    sorted_x = sorted(values.items(), key=operator.itemgetter(1), reverse=True)
    clear("Values sorted by number of times they 'outcompeted' others.")
    print("A total of {0} comparisons has been done.\n".format(sum(values.values())))
    # print("{0:>4}: Sum".format(sum(values.values())))
    print("----- ---------------")
    for k, v in sorted_x:
        print("{1:>4}: {0}".format(k, v))


if __name__ == "__main__":
    main()
