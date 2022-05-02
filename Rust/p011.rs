/*
In the 20 x 20 grid below, four numbers along a diagonal line have been marked in red.

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

The product of these numbers is 26 x 63 x 78 x 14 = 1788696.
What is the greatest product of four adjacent numbers in the same direction
(up, down, left, right, or diagonally) in the 20 x 20 grid?
*/

use std::collections::VecDeque;

type Matrix<T> = Vec<Vec<T>>;

fn products(vectors: Vec<Vec<u64>>, adj: usize) -> Vec<u64> {
    vectors
        .iter()
        .filter(|row| row.len() >= adj)
        .map(|row| max_adj_product(row, adj))
        .collect()
}

fn get_answer(matrix: &String, adj: usize) -> u64 {
    let max = |x, y| {
        if x > y {
            x
        } else {
            y
        }
    };

    let matrix = matrix_from_string(matrix);
    let matrix_t = transposed(&matrix);
    let diagonals = get_diagonals(&matrix);
    let counter_diagonals = get_counter_diagonals(&matrix);

    let mut max_prod = 1;
    for p in products(matrix, adj) {
        max_prod = max(p, max_prod);
    }
    for p in products(matrix_t, adj) {
        max_prod = max(p, max_prod);
    }
    for p in products(diagonals, adj) {
        max_prod = max(p, max_prod);
    }
    for p in products(counter_diagonals, adj) {
        max_prod = max(p, max_prod);
    }
    max_prod
}

fn transposed(matrix: &Matrix<u64>) -> Matrix<u64> {
    let mut transposed_matrix = vec![];
    let size;
    if let Some(row) = matrix.get(0) {
        size = row.len();
        transposed_matrix.reserve(size);
    } else {
        return transposed_matrix;
    }

    for i in 0..size {
        let mut v = vec![];
        v.reserve(matrix.len());

        for row in matrix {
            v.push(row[i]);
        }
        transposed_matrix.push(v);
    }
    transposed_matrix
}

fn matrix_from_string(string: &String) -> Matrix<u64> {
    string
        .split('\n')
        .map(|string| string.trim())
        .filter(|&string| string != "")
        .map(|string| {
            string
                .split_whitespace()
                .map(|str_num| str_num.parse::<u64>().unwrap())
                .collect()
        })
        .collect()
}

fn max_adj_product(v: &Vec<u64>, adj: usize) -> u64 {
    if v.len() <= adj {
        let mut prod = 1;
        for &n in v {
            if n == 0 {
                return 0;
            } else {
                prod *= n;
            }
        }
        return prod;
    }

    let max = |x, y| {
        if x > y {
            x
        } else {
            y
        }
    };

    let mut iterator = v.iter();
    let mut prod = 1;
    let mut deq: VecDeque<u64> = VecDeque::new();

    for _ in 0..adj {
        let &num = iterator.next().unwrap();
        if num == 0 {
            prod = 0;
            deq.clear();
            break;
        }
        prod *= num;
        deq.push_back(num);
    }

    let mut max_prod: u64 = 1;
    for &num in iterator {
        if num == 0 {
            deq.clear();
            continue;
        }
        if deq.is_empty() {
            prod = num
        } else {
            let prev = deq.pop_front().unwrap();
            prod /= prev;
            prod *= num;
        }
        deq.push_back(num);
        if deq.len() == adj {
            max_prod = max(prod, max_prod);
        }
    }
    max_prod
}

fn get_diagonals(matrix: &Matrix<u64>) -> Vec<Vec<u64>> {
    let mut diagonals = vec![];
    let dim0 = matrix.len();
    let dim1;
    let diag_len;

    if let Some(row) = matrix.get(0) {
        dim1 = row.len();
        diag_len = dim0 + dim1 - 1;
        diagonals.reserve(diag_len);
    } else {
        return diagonals;
    }

    let mut count = 0;
    for mut col in (0..dim1).rev() {
        if count < dim0 {
            count += 1;
        }
        let mut diag = vec![];
        diag.reserve(count);

        for row in 0..count {
            let el = matrix[row][col];
            diag.push(el);
            col += 1;
            if col == dim1 {
                break;
            }
        }
        diagonals.push(diag);
    }
    let mut row_start = 0;
    for _ in diagonals.len()..diag_len {
        row_start += 1;
        let mut diag = vec![];
        diag.reserve(dim0 - row_start);

        let mut col = 0;
        for row in row_start..dim0 {
            let el = matrix[row][col];
            diag.push(el);
            col += 1;
        }
        diagonals.push(diag);
    }
    diagonals
}

fn get_counter_diagonals(matrix: &Matrix<u64>) -> Vec<Vec<u64>> {
    let mut diagonals = vec![];
    let dim0 = matrix.len();
    let dim1;
    let diag_len;

    if let Some(row) = matrix.get(0) {
        dim1 = row.len();
        diag_len = dim0 + dim1 - 1;
        diagonals.reserve(diag_len);
    } else {
        return diagonals;
    }

    let mut count = 0;
    for mut col in 0..dim1 {
        if count < dim0 {
            count += 1;
        }
        let mut diag = vec![];
        diag.reserve(count);

        for row in 0..count {
            let el = matrix[row][col];
            diag.push(el);
            if col == 0 {
                break;
            }
            col -= 1;
        }
        diagonals.push(diag);
    }
    let mut start_row = 0;
    for _ in diagonals.len()..diag_len {
        start_row += 1;
        let mut diag = vec![];
        diag.reserve(dim0 - start_row);

        for row in start_row..dim0 {
            let el = matrix[row][dim1 - row];
            diag.push(el);
        }
        diagonals.push(diag)
    }
    diagonals
}

fn main() {
    let matrix = "
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
    "
    .to_string();

    let adj = 4;
    let answer = get_answer(&matrix, adj);
    println!("{answer}");
}
