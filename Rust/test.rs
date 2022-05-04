use std::fs;
use std::process::{Command, Output};

fn main() {
    compile_all(".");
}

fn compile_all(dir: &str) {
    let files = listdir(dir);
    let src_files = files.iter().filter(|s| s.ends_with(".rs"));
    for src in src_files {
        test_compilation(src.as_str());
    }
}

fn compile_rs(src: &str) -> Result<Output, std::io::Error> {
    let mut command = Command::new("rustc");
    command.arg(src).output()
}

fn test_compilation(src: &str) {
    let output = compile_rs(src);
    match output {
        Ok(out) => {
            if !out.status.success() {
                println!("{src}:\n\t{:?}\n", out)
            }
        }
        Err(error) => println!("{src}:\n\tErr({:?})\n", error),
    }
}

fn listdir(dir: &str) -> Vec<String> {
    let paths = fs::read_dir(dir)
        .unwrap()
        .map(|result| {
            result
                .unwrap()
                .path()
                .into_os_string()
                .into_string()
                .unwrap()
        })
        .collect();

    paths
}
