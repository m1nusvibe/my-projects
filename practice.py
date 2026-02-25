# Текстовый калькулятор — создайте программу,
# которая выполняет арифметические операции, введенные в виде текста.
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
    if not tokens: return 0
    if len(tokens) == 1: return tokens[0]
    i = 0
    while i < len(tokens):

        if tokens[i] == '*' or tokens[i] == '/':
            a, _, b = tokens[i-1:i+2]
            if tokens[i] == '*':
                result = a*b
                tokens[i-1] = result
                del tokens[i:i+2]
            elif tokens[i] == '/':
                result = a/b
                tokens[i-1] = result
                del tokens[i:i+2]
        else:
            i += 1
    i = 0
    while i < len(tokens):
        if tokens[i] == '+' or tokens[i] == '-':
            a, _, b = tokens[i-1:i+2]
            if tokens[i] == '+':
                result = a+b
                tokens[i-1] = result
                del tokens[i:i+2]
            elif tokens[i] == '-':
                result = a-b
                tokens[i-1] = result
                del tokens[i:i+2]
        else:
            i += 1
    print(tokens[0])
    return tokens[0]
calculate(tokenize("семь плюс 9 разделить на 3"))
