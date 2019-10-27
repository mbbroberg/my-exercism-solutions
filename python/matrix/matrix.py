class Matrix(object):
    """A simple columnar string parser"""

    matrix = []

    def __init__(self, matrix_string):
        self.matrix = matrix_string.split("\n")
        for n, row in enumerate(self.matrix):
            self.matrix[n] = row.split(" ")

    def row(self, index):
        int_row = []
        try:
            for item in self.matrix[index - 1]:
                int_row.append(int(item))
            return int_row
        except IndexError:
            print(f"Row value {index} is out of range of the matrix.")
        else:
            print("Something went terribly wrong.")

    def column(self, index):
        int_col = []
        try:
            for row in self.matrix:
                int_col.append(int(row[index - 1]))
            return int_col
        except IndexError:
            print(f"Column value {index} is out of range of the matrix.")
        else:
            print("Something went terribly wrong.")