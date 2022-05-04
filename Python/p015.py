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


def route_matrix(shape: int) -> Matrix:
    m: Matrix = make_matrix(shape)
    m[0] = [1]*len(m[0])
 
    for i in range(1, len(m)):
        m[i][0] = 1
    
    for i in range(1, len(m)):
        for j in range(1, len(m[i])):
            m[i][j] = m[i-1][j] + m[i][j-1]
 
    return m


def main():
    shape = 1 + 20
    matrix = route_matrix(shape)
    
    answer = matrix[-1][-1]
    print(answer)


if __name__ == '__main__':
    main()

