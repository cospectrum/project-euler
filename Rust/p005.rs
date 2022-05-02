/*
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
*/

use std::collections::{HashMap, HashSet};

fn main() {
    const N: u64 = 20;

    let mut union: HashMap<u64, u32> = HashMap::new();
    let mut num: HashMap<u64, u32>;

    for n in 1..=N {
        num = get_factorization(n);
        union = max_union(&union, &num);
    }

    let answer = map_to_num(&union);
    println!("{answer}");
}

fn max_union(map1: &HashMap<u64, u32>, map2: &HashMap<u64, u32>) -> HashMap<u64, u32> {
    let max = |x, y| {
        if x > y {
            x
        } else {
            y
        }
    };

    let mut union = HashMap::new();
    let keys = keys_union(&map1, &map2);

    for key in keys {
        match (map1.get(&key), map2.get(&key)) {
            (Some(&v1), Some(&v2)) => union.insert(key, max(v1, v2)),
            (None, Some(&v)) | (Some(&v), None) => union.insert(key, v),
            (None, None) => None,
        };
    }
    union
}

fn keys_union(map1: &HashMap<u64, u32>, map2: &HashMap<u64, u32>) -> HashSet<u64> {
    let keys1: HashSet<u64> = map1.keys().map(|&x| x).collect();
    let keys2: HashSet<u64> = map2.keys().map(|&x| x).collect();

    let keys = keys1.union(&keys2).map(|&x| x).collect();
    keys
}

fn get_factorization(num: u64) -> HashMap<u64, u32> {
    let mut n = num;
    let mut map = HashMap::new();

    while n != 1 {
        for d in 2..=n {
            if n % d == 0 {
                n /= d;
                match map.get(&d) {
                    Some(&pow) => map.insert(d, pow + 1),
                    None => map.insert(d, 1),
                };
                break;
            }
        }
    }
    map
}

fn map_to_num(map: &HashMap<u64, u32>) -> u64 {
    let mut product = 1;
    for key in map.keys() {
        if let Some(&power) = map.get(key) {
            product *= key.pow(power);
        }
    }
    product
}
