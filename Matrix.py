def vector_product(v1, v2):
    len_v1 = len(v1)
    result = []
    if len_v1 != len(v2):
        return "Error: Vectors must be same size"

    for i in range(len_v1):
        result[i] = v1[i] * v2[i]

    return result


class Matrix:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.matrix = [[0] * self.width for _ in range(height)]

    def __str__(self):
        return str(self.matrix)

    def get_height(self):
        return self.height

    def get_width(self):
        return self.width

    def get_matrix(self):
        return self.matrix

    def display(self):
        for row in self.matrix:
            print(row)

    def transpose(self):
        w, h = self.get_width(), self.get_height()
        i = 0
        transposed = Matrix(w, h)
        for row in self.matrix:
            k = 0
            for j in range(w):
                transposed.matrix[j][i] = row[k]
                k += 1
            i += 1

        return transposed

    def get_diagonal(self):
        diagonal = []
        length = min(self.get_width(), self.get_height())
        for i in range(length):
            diagonal.append(self.matrix[i][i])

        return diagonal

    def get_trace(self):
        trace = 0
        for num in self.get_diagonal():
            trace += num

        return trace

    def is_null(self):
        null_test = Matrix(self.get_width(), self.get_height())

        return self.matrix == null_test

    def get_identity_matrix(self, size):
        identity_matrix = Matrix(size, size)
        for i in range(size):
            identity_matrix.matrix[i][i] = 1

        return identity_matrix

    def matrix_sum(self, matrix_2, sign):
        m1_width = self.get_width()
        m1_height = self.get_width()
        if m1_width != matrix_2.get_width() or m1_height != matrix_2.get_height():
            return "Error: matrices not the same size"

        result = Matrix(m1_width, m1_height)

        for row_iter in range(m1_height):
            for col_iter in range(m1_width):
                result.matrix[row_iter][col_iter] = eval(str(self.matrix[row_iter][col_iter]) + sign +
                                                         str(matrix_2.matrix[row_iter][col_iter]))

        return result

    def scalar_product(self, scalar):
        result = Matrix(self.get_width(), self.get_height())
        for row in self.matrix:
            for i in range(self.get_width()):
                result.matrix[i] = row[i] * scalar

        return result

    # Look into updating using vector product function
    def matrix_product(self, matrix_2):
        if self.get_width() != matrix_2.get_height():
            return "Error: matrices not the same size"

        result_matrix = Matrix(self.get_width(), self.get_height())
        m2_transposed = matrix_2.transpose()

        for row in range(self.get_height()):
            for num in range(self.get_width()):
                for j in range(self.get_width()):
                    result_matrix.matrix[row][num] += self.matrix[row][j] * m2_transposed.matrix[num][j]

        return result_matrix

    def get_lu_matrices(self):
        height = self.get_height()
        width = self.get_width()

        if height != width:
            return "Error: Only get LU from square matrix"

        lower = Matrix(width, height)
        upper = Matrix(width, height)

        for i in range(width):
            lower.matrix[i][i] = 1

        # li * uj = mi,j
        # li = mi,j / uj
        # uj = m1,j / li

    # ONLY DOES 3X3 MATRICES NEEDS IMPROVEMENT USE LU FACTORISATION AND TAKE PRODUCT OF DIAGONAL
    def determinant(self):
        if self.get_height() != self.get_width():
            return "Error: Cannot use non-square matrix"

        positives = (self.matrix[0][0] * self.matrix[1][1] * self.matrix[2][2]) + \
                    (self.matrix[1][0] * self.matrix[2][1] * self.matrix[0][2]) + \
                    (self.matrix[2][0] * self.matrix[0][1] * self.matrix[1][2])

        negatives = -(self.matrix[0][2] * self.matrix[1][1] * self.matrix[2][0]) - \
                     (self.matrix[0][1] * self.matrix[1][0] * self.matrix[2][2]) - \
                     (self.matrix[0][0] * self.matrix[1][2] * self.matrix[2][1])

        return positives + negatives


if __name__ == "__main__":
    m1 = Matrix(3, 3)
    m1.matrix = [[1,2,3] for _ in range(3)]
    m2 = Matrix(3, 3)
    m2.matrix = [[3,2,1] for _ in range(3)]

    producted = m1.matrix_product(m2)

    producted.display()

    m3 = Matrix(3,3)
    m3.matrix = [[1, 2, 3], [4, 5, 6], [7, 8, 99]]

    print(m3.determinant())
