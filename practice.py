import operator

numbers = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6,
           'семь': 7, 'восемь': 8, 'девать': 9}
operations = {'+': operator.add, '-': operator.sub, '*': operator.mul, '/': operator.truediv}

operations_symbol = {'минус': '-',
                     'плюс': '+',
                     'умножить': '*',
                     'разделить': '/'}

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
    while len(tokens) > 0:
        for i in range(0, len(tokens)):
            if tokens[i] == '+':
                result = tokens[i-1] + tokens[i+1]
            elif tokens[i] == '-':
                result = tokens[i-1] - tokens[i+1]
    return result
calculate(tokenize("два плюс три минус один"))