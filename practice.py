# калькулятор который
import operator

numbers = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6,
           'семь': 7, 'восемь': 8, 'девять': 9}
operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

operations_symbol = {'минус': '-',
                     'плюс': '+',
                     'умножить': '*',
                     'разделить': '/',
                     'делить': '/',
                     'добавить': '+',
                     'прибавить': '+',
                     'домножить' : '*',
                     'вычесть': '-',
                     'поделить': '/'}

def tokenize(text):
    ready_text = []
    splits_text = text.split()

    for words in splits_text:
        if words in numbers.keys():
            ready_text.append(numbers[words])

        elif words.isdigit():
            ready_text.append(int(words))

        elif words in operations.keys():
            ready_text.append(words)

        elif words in operations_symbol:
            ready_text.append(operations_symbol[words])

    return ready_text


def calculate(tokens):
    result = 0
    while '*' in tokens or '/' in tokens:
        if '*' in tokens:
            idx = tokens.index('*')
            a, _, b = tokens[idx - 1 : idx + 2]
            result = a * b
            del tokens[idx - 1 : idx + 2]
            tokens.append(result)
        elif '/' in tokens:
            idx = tokens.index('/')
            a, _, b = tokens[idx - 1:idx + 2]
            result = a / b
            del tokens[idx - 1:idx + 2]
            tokens.append(result)

    while '+' in tokens or '-' in tokens:
        if '+' in tokens:
            idx = tokens.index('+')
            a, _, b = tokens[idx - 1:idx + 2]
            result = a + b
            del tokens[idx - 1:idx + 2]
            tokens.append(result)
        elif '-' in tokens:
            idx = tokens.index('-')
            a, _, b = tokens[idx - 1:idx + 2]
            result = a - b
            del tokens[idx - 1:idx + 2]
            tokens.append(result)

    print(result)
    return result
calculate(tokenize("два плюс пять разделить пять"))
