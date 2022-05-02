/*
The four adjacent digits in the 1000-digit number that have the greatest
product are 9 × 9 × 8 × 9 = 5832.
    73167176531330624919225119674426574742355349194934
    96983520312774506326239578318016984801869478851843
    85861560789112949495459501737958331952853208805511
    12540698747158523863050715693290963295227443043557
    66896648950445244523161731856403098711121722383113
    62229893423380308135336276614282806444486645238749
    30358907296290491560440772390713810515859307960866
    70172427121883998797908792274921901699720888093776
    65727333001053367881220235421809751254540594752243
    52584907711670556013604839586446706324415722155397
    53697817977846174064955149290862569321978468622482
    83972241375657056057490261407972968652414535100474
    82166370484403199890008895243450658541227588666881
    16427171479924442928230863465674813919123162824586
    17866458359124566529476545682848912883142607690042
    24219022671055626321111109370544217506941658960408
    07198403850962455444362981230987879927244284909188
    84580156166097919133875499200524063689912560717606
    05886116467109405077541002256983155200055935729725
    71636269561882670428252483600823257530420752963450
Find the thirteen adjacent digits in the 1000-digit number that have the
greatest product. What is the value of this product?
*/

use std::collections::VecDeque;

fn clean_string(num: &String) -> String {
    num.chars().filter(|ch| ch.is_digit(10)).collect()
}

fn str_to_vec(string: &str) -> Vec<u8> {
    let digits = string
        .chars()
        .map(|ch| ch.to_digit(10).unwrap() as u8)
        .collect();
    digits
}

fn find_max_product(num: &String, adj: usize) -> u64 {
    let max = |x, y| {
        if x > y {
            x
        } else {
            y
        }
    };

    let mut digits: Vec<u8>;
    let mut deq: VecDeque<u8> = VecDeque::new();
    let mut max_prod: u64 = 0;
    let mut prod: u64;

    let string = clean_string(num);
    let sliced_str: Vec<&str> = string.split('0').filter(|&string| string != "").collect();

    for slice in sliced_str {
        deq.clear();
        prod = 1;
        digits = str_to_vec(slice);

        if digits.len() > adj {
            for &digit in &digits[..adj] {
                prod *= digit as u64;
                deq.push_back(digit);
            }
            max_prod = max(prod, max_prod);

            for &digit in &digits[adj..] {
                let prev = deq.pop_front().unwrap() as u64;
                prod /= prev;
                prod *= digit as u64;

                max_prod = max(prod, max_prod);
                deq.push_back(digit);
            }
        } else {
            for digit in digits {
                prod *= digit as u64;
            }
            max_prod = max(prod, max_prod);
        }
    }
    max_prod
}

fn main() {
    let number = "
        73167176531330624919225119674426574742355349194934
        96983520312774506326239578318016984801869478851843
        85861560789112949495459501737958331952853208805511
        12540698747158523863050715693290963295227443043557
        66896648950445244523161731856403098711121722383113
        62229893423380308135336276614282806444486645238749
        30358907296290491560440772390713810515859307960866
        70172427121883998797908792274921901699720888093776
        65727333001053367881220235421809751254540594752243
        52584907711670556013604839586446706324415722155397
        53697817977846174064955149290862569321978468622482
        83972241375657056057490261407972968652414535100474
        82166370484403199890008895243450658541227588666881
        16427171479924442928230863465674813919123162824586
        17866458359124566529476545682848912883142607690042
        24219022671055626321111109370544217506941658960408
        07198403850962455444362981230987879927244284909188
        84580156166097919133875499200524063689912560717606
        05886116467109405077541002256983155200055935729725
        71636269561882670428252483600823257530420752963450
    "
    .to_string();

    let answer = find_max_product(&number, 13);
    println!("{}", answer);
}