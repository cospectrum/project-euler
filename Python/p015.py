"""
Starting in the top left corner of a 2×2 grid, and only being able to move to
the right and down, there are exactly 6 routes to the bottom right corner.
    ______           ___           ___
          |             |             |
          |             |             |___
          |             |                 |
          |             |___              |

    |               |              |
    |               |___           |______
    |                   |                 |
    |______             |___              |

How many such routes are there through a 20×20 grid?
"""

from typing import List, Any

Matrix = List[List[Any]]


def make_matrix(shape: int) -> Matrix:
    matrix = [[0]*shape for _ in range(shape)]
    return matrix


def get_route_matrix(shape: int) -> Matrix:
    matrix = make_matrix(shape)
    matrix[0] = [1]*len(matrix[0])
    for i in range(1, len(matrix)):
        matrix[i][0] = 1
    for i in range(1, len(matrix)):
        for j in range(1, len(matrix[i])):
            matrix[i][j] = matrix[i-1][j] + matrix[i][j-1]
    return matrix


def main():
    shape = 1 + 20
    matrix = get_route_matrix(shape)
    answer = matrix[-1][-1]
    print(answer)


if __name__ == '__main__':
    main()
