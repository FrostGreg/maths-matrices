def create(width, height):
    matrix = [[0] * width for _ in range(height)]
    return matrix


#Test function
def initiate():
    m1 = create(3, 3)
    for i in range(9):
        m1[i // 3][i % 3] = i + 1

    return m1


def display(matrix):
    for row in matrix:
        print(row)


def getheight(matrix):
    return len(matrix)


def getwidth(matrix):
    return len(matrix[0])


def vector_product(v1, v2):
    len_v1 = len(v1)
    result = []
    if len_v1 != len(v2):
        return "Error: Vectors must be same size"

    for i in range(len_v1):
        result[i] = v1[i] * v2[i]

    return result


def transpose(matrix):
    w = getwidth(matrix)
    h = getheight(matrix)
    i = 0
    transposed = create(w, h)
    for row in matrix:
        k = 0
        for j in range(w):
            transposed[j][i] = row[k]
            k += 1
        i += 1

    return transposed


def get_diagonal(matrix):
    diagonal = []
    length = min(getwidth(matrix), getheight(matrix))
    for i in range(length):
        diagonal.append(matrix[i][i])

    return diagonal


def get_trace(matrix):
    trace = 0
    for num in get_diagonal(matrix):
        trace += num

    return trace


def is_null(matrix):
    null = True
    for row in matrix:
        for num in row:
            if num != 0:
                null = False
                break

    return null


def get_identity_matrix(size):
    identity_matrix = create(size, size)
    for i in range(size):
        identity_matrix[i][i] = 1

    return identity_matrix


def matrix_sum(m1, m2, sign):
    m1_width = getwidth(m1)
    m1_height = getwidth(m1)
    if m1_width != getwidth(m2) or m1_height != getheight(m2):
        return "Error: matrices not the same size"

    result = create(m1_width, m1_height)

    for row_iter in range(m1_height):
        for col_iter in range(m1_width):
            result[row_iter][col_iter] = eval(str(m1[row_iter][col_iter]) + sign + str(m2[row_iter][col_iter]))

    return result


def scalar_product(matrix, scalar):
    for row in matrix:
        for i in range(getwidth(matrix)):
            row[i] *= scalar

    return matrix


#Look into updating using vector product function
def matrix_product(m1, m2):
    if getwidth(m1) != getheight(m2):
        return "Error: matrices not the same size"

    result_matrix = create(getwidth(m1), getheight(m1))
    m2_transposed = transpose(m2)

    for row in range(len(m1)):
        for num in range(len(m1[row])):
            for j in range(len(m1[row])):
                result_matrix[row][num] += m1[row][j] * m2_transposed[num][j]

    return result_matrix


def get_lu_matrices(matrix):
    height = getheight(matrix)
    width = getwidth(matrix)

    if height != width:
        return "Error: Only get LU from square matrix"

    lower = create(width, height)
    upper = create(width, height)

    for i in range(width):
        lower[i][i] = 1

    #li * uj = mi,j
    #li = mi,j / uj
    #uj = m1,j / li


#ONLY DOES 3X3 MATRICES NEEDS IMPROVEMENT USE LU FACTORISATION AND TAKE PRODUCT OF DIAGONAL
def determinant(matrix):
    if getheight(matrix) != getwidth(matrix):
        return "Error: Cannot use non-square matrix"

    positives = (matrix[0][0] * matrix[1][1] * matrix[2][2]) + (matrix[1][0] * matrix[2][1] * matrix[0][2]) + (matrix[2][0] * matrix[0][1] * matrix[1][2])
    negatives = -(matrix[0][2] * matrix[1][1] * matrix[2][0]) - (matrix[0][1] * matrix[1][0] * matrix[2][2]) - (matrix[0][0] * matrix[1][2] * matrix[2][1])

    return positives + negatives


m1 = initiate()
m2 = initiate()

producted = matrix_product(m1, m2)

display(producted)

m3 = [[1,2,3],[4,5,6],[7,8,99]]

print(determinant(m3))

# this is test code for git