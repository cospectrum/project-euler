"""
If the numbers 1 to 5 are written out in words: one, two, three, four, five,
then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in
words, how many letters would be used?

NOTE: Do not count spaces or hyphens. For example, 342
(three hundred and forty-two) contains 23 letters and 115
(one hundred and fifteen) contains 20 letters. The use of "and" when writing
out numbers is in compliance with British usage.
"""


def get_words():
    words = '''
    one, two, three, four, five, six, seven, eight, nine
    eleven, twelve, thirteen, fourteen, fifteen, sixteen, seventeen, eighteen, nineteen
    ten, twenty, thirty, forty, fifty, sixty, seventy, eighty, ninety
    '''
    
    words = [
        line.strip().split(', ')
        for line in words.split('\n')
        if line.strip()
    ]
    
    dict_ = {
        '1-9': words[0],
        '11-19': words[1],
        'zeros': words[2],
    }
    return dict_


def get_numbers_dict() -> dict:
    words = get_words()
    
    numbers = words['1-9'] + ['ten'] + words['11-19']
    numbers += [
        ' '.join([zero_num, digit]).rstrip()
        for zero_num in words['zeros'][1:]
        for digit in [''] + words['1-9']
    ]
    
    for num in words['1-9']:
        prefix = f'{num} hundred'
        numbers.append(prefix)

        numbers += [f'{prefix} and {word}' for word in words['1-9'] + ['ten']]
        numbers += [f'{prefix} and {word}' for word in words['11-19']]
        
        for zero_num in words['zeros'][1:]:
            numbers += [
                f'{prefix} and {zero_num} {digit}'.rstrip()
                for digit in [''] + words['1-9']
            ]

    numbers.append('one thousand')
    
    numbers_dict = {
        index + 1: number
        for index, number in enumerate(numbers)
    }
    return numbers_dict


def get_answer() -> int:
    numbers = get_numbers_dict().values()
    
    answer = len(''.join(num.replace(' ', '') for num in numbers))
    return answer


def main():
    answer = get_answer()
    print(answer)


if __name__ == '__main__':
    main()

