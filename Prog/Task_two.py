#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import random


class IllegalRowValue(Exception):
    def __init__(self, row, message="Illegall count of Row"):
        self.row = row
        self.message = message
        super(IllegalRowValue, self).__init__(message)

    def __str__(self):
        return f"{self.row} -> {self.message}"


class IllegalColValue:
    def __init__(self, col, message="Illegall count of Col"):
        self.col = col
        self.message = message
        super(IllegalColValue, self).__init__(message)

    def __str__(self):
        return f"{self.col} -> {self.message}"


class IllegalStartValue:
    def __init__(self, start, message="Illegall start value"):
        self.start = start
        self.message = message
        super(IllegalStartValue, self).__init__(message)

    def __str__(self):
        return f"{self.start} -> {self.message}"


class IllegalEndValue:
    def __init__(self, end, message="Illegall end value"):
        self.end = end
        self.message = message
        super(IllegalEndValue, self).__init__(message)

    def __str__(self):
        return f"{self.end} -> {self.message}"


class Randommatrix:
    def __init__(self, col, row, start, end):
        self.col = col
        self.row = row
        self.start = start
        self.end = end

    def generate_matrix(self):
        if self.row == 0:
            raise IllegalRowValue(self.row)

        if self.col == 0:
            raise IllegalColValue(self.col)

        result = []

        for i in range(self.row):
            result.append([])

        for i in result:
            counter = 0
            while counter != self.col:
                i.append(random.randint(self.start, self.end))
                counter += 1

        self.matrix = result
        return result

    def show_matrix(self):
        for i in self.matrix:
            print(i)


def main():
    matrix = Randommatrix(5, 4, 1, 5)
    matrix.generate_matrix()
    matrix.show_matrix()


if __name__ == "__main__":
    main()