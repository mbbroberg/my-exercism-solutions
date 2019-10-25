class Matrix(object):
    """A simple columnar string parser"""
    matrix = []

    def __init__(self, matrix_string):
        self.matrix = matrix_string.split("\n")
        for n, row in enumerate(self.matrix):
            self.matrix[n] = row.split(' ')
        
    def row(self, index):
        pass

    def column(self, index):
        pass


#  Matrix("1 2 3\n4 5 6\n7 8 9")
#  self.assertEqual(matrix.column(3), [3, 6, 9])
x = Matrix('1 2 3\n4 5 6\n7 8 9')
# returns: [['1', '2', '3'], ['4', '5', '6'], ['7', '8', '9']]
