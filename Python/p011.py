"""
In the 20×20 grid below, four numbers along a diagonal line have been marked in red.

    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48

The product of these numbers is 26 × 63 × 78 × 14 = 1788696.
What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20×20 grid?
"""

from collections import deque


def max_product(iterable_obj, *, adjacency: int):
    assert adjacency > 0
    
    queue = deque()
    iterator = iter(iterable_obj)
    
    product = 1
    for _ in range(adjacency):
        num = next(iterator)
        if num == 0:
            product = 0
            queue = deque()
            break
        product *= num
        queue.append(num)
    
    great_product = product
    for num in iterator:
        if num == 0:
            queue = deque()
            continue
        if len(queue) == 0:
            product = num
        else:
            product *= num/queue.popleft()
        
        queue.append(num)
        if len(queue) == adjacency:
            great_product = max(product, great_product)
    
    return great_product


def matrix_from_string(matrix: str) -> list:
    matrix_generator = (line.strip() for line in matrix.splitlines())
    
    matrix = [
        [int(num) for num in row.split()]
        for row in matrix_generator if row
    ]
    return matrix


def transpose_matrix(matrix: list) -> list:
    transposed_matrx = [
        [row[i] for row in matrix]
        for i in range(len(matrix[0]))
    ]
    return transposed_matrx


def get_diagonals(matrix: list) -> list:
    diagonals = []
    matrix_len = len(matrix)
    diagonals_len = 2*matrix_len - 1
    
    for i in range(diagonals_len):
        if i < matrix_len:
            col_iter = range(matrix_len-i-1, matrix_len)
            row_iter = range(0, i+1)
        else:
            col_iter = range(0, diagonals_len-i)
            row_iter = range(i % matrix_len + 1, matrix_len)
        
        diagonal = [matrix[row][col] for row, col in zip(row_iter, col_iter)]
        diagonals.append(diagonal)
    
    return diagonals


def get_counter_diagonals(matrix: list) -> list:
    diagonals = []
    matrix_len = len(matrix)
    diagonals_len = 2*matrix_len - 1
    
    for i in range(diagonals_len):
        if i < matrix_len:
            col_iter = range(i, -1, -1)
            row_iter = range(0, i+1)
        else:
            col_iter = range(matrix_len-1, -1, -1)
            row_iter = range(i % matrix_len + 1, matrix_len)
        
        diagonal = [matrix[row][col] for row, col in zip(row_iter, col_iter)]
        diagonals.append(diagonal)
    
    return diagonals


def get_answer(matrix, adjacency: int):
    if isinstance(matrix, str):
        matrix = matrix_from_string(matrix)
    
    transposed_matrix = transpose_matrix(matrix)
    diagonals = get_diagonals(matrix)
    counter_diagonals = get_counter_diagonals(matrix)

    max_column_prod = max(
        max_product(column, adjacency=adjacency)
        for column in matrix if len(column) >= adjacency
    )
    max_row_prod = max(
        max_product(row, adjacency=adjacency)
        for row in transposed_matrix if len(row) >= adjacency
    )
    max_diag_prod = max(
        max_product(diag, adjacency=adjacency)
        for diag in diagonals if len(diag) >= adjacency
    )
    max_counter_diag_prod = max(
        max_product(diag, adjacency=adjacency)
        for diag in counter_diagonals if len(diag) >= adjacency
    )

    greatest_product = max(
        max_column_prod, max_row_prod, max_diag_prod, max_counter_diag_prod
    )
    
    return greatest_product


def main():
    matrix = '''
    08 02 22 97 38 15 00 40 00 75 04 05 07 78 52 12 50 77 91 08
    49 49 99 40 17 81 18 57 60 87 17 40 98 43 69 48 04 56 62 00
    81 49 31 73 55 79 14 29 93 71 40 67 53 88 30 03 49 13 36 65
    52 70 95 23 04 60 11 42 69 24 68 56 01 32 56 71 37 02 36 91
    22 31 16 71 51 67 63 89 41 92 36 54 22 40 40 28 66 33 13 80
    24 47 32 60 99 03 45 02 44 75 33 53 78 36 84 20 35 17 12 50
    32 98 81 28 64 23 67 10 26 38 40 67 59 54 70 66 18 38 64 70
    67 26 20 68 02 62 12 20 95 63 94 39 63 08 40 91 66 49 94 21
    24 55 58 05 66 73 99 26 97 17 78 78 96 83 14 88 34 89 63 72
    21 36 23 09 75 00 76 44 20 45 35 14 00 61 33 97 34 31 33 95
    78 17 53 28 22 75 31 67 15 94 03 80 04 62 16 14 09 53 56 92
    16 39 05 42 96 35 31 47 55 58 88 24 00 17 54 24 36 29 85 57
    86 56 00 48 35 71 89 07 05 44 44 37 44 60 21 58 51 54 17 58
    19 80 81 68 05 94 47 69 28 73 92 13 86 52 17 77 04 89 55 40
    04 52 08 83 97 35 99 16 07 97 57 32 16 26 26 79 33 27 98 66
    88 36 68 87 57 62 20 72 03 46 33 67 46 55 12 32 63 93 53 69
    04 42 16 73 38 25 39 11 24 94 72 18 08 46 29 32 40 62 76 36
    20 69 36 41 72 30 23 88 34 62 99 69 82 67 59 85 74 04 36 16
    20 73 35 29 78 31 90 01 74 31 49 71 48 86 81 16 23 57 05 54
    01 70 54 71 83 51 54 69 16 92 33 48 61 43 52 01 89 19 67 48
    '''
    adjacency = 4

    answer = get_answer(matrix, adjacency)
    answer = int(answer)
    print(answer)


if __name__ == '__main__':
    main()

