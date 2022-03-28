import os
import subprocess
from typing import List


def parse_problems(*, answers_file) -> List[dict]:
    """Parse answers.txt file with number, name, answer"""
    
    with open(answers_file, 'r') as f:
        lines = f.readlines()
    
    lines = [
        [cell.strip() for cell in line.split(',')]
        for line in lines[1:]
    ]
    
    parsed_lines: List[dict] = [
        {'number': int(number), 'name': name, 'answer': int(answer)}
        for number, name, answer in lines
    ]
    return parsed_lines


def parse_src_files(
    *,
    folder: str,
    endswith: str,
    startswith: str = '',
) -> List[str]:
    """Parse all source files in a folder"""

    listdir: List[str] = os.listdir(folder)
    
    src_files: List[str] = [
        src for src in listdir
        if src.endswith(endswith) and src.startswith(startswith)
    ]
    
    src_files.sort()
    return src_files


def check_answers(
    *,
    answers_file: str,
    relative_src_folder: str,
    endswith: str,
    startswith: str = '',
) -> None:

    problems = parse_problems(answers_file=answers_file)
    
    src_files = parse_src_files(
        folder=relative_src_folder,
        endswith=endswith,
        startswith=startswith
    )
    
    for problem, src_file in zip(problems, src_files):
        number, name, answer = problem.values()
        
        command: str = f'python3 {relative_src_folder}/{src_file}'
        args = command.split()

        result = subprocess.run(args, stdout=subprocess.PIPE)
        stdout = result.stdout.decode()

        success: bool = str(answer).strip() == stdout.strip()
        print(f'{success}: {number}. {name}.')
        if not success:
            print(f'\tright answer: {answer}, got answer: {stdout}')
    return


def main():
    check_answers(
        answers_file='../answers.txt',
        relative_src_folder='.',
        endswith='.py',
        startswith='p'
    )
    return


if __name__ == '__main__':
    main()

