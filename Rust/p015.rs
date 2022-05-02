/*
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
*/

type Matrix<T> = Vec<Vec<T>>;

fn main() {
    let shape = 1 + 20;
    let mut matrix = make_route_matrix(shape);
    let answer = matrix[shape - 1].pop().unwrap();
    println!("{}", answer);
}

fn make_matrix(shape: usize) -> Matrix<u64> {
    let mut matrix = vec![];
    matrix.reserve(shape);

    for _ in 0..shape {
        let row = vec![0; shape];
        matrix.push(row);
    }
    matrix
}

fn make_route_matrix(shape: usize) -> Matrix<u64> {
    let mut matrix = make_matrix(shape);
    matrix[0] = vec![1; matrix[0].len()];

    for i in 1..matrix.len() {
        matrix[i][0] = 1;
    }

    for i in 1..matrix.len() {
        for j in 1..matrix[i].len() {
            matrix[i][j] = matrix[i - 1][j] + matrix[i][j - 1];
        }
    }
    matrix
}
