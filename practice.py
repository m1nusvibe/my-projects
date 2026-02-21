import operator

numbers = {'ноль': 0, 'один': 1, 'два': 2, 'три': 3, 'четыре': 4, 'пять': 5, 'шесть': 6,
           'семь': 7, 'восемь': 8, 'девять': 9}
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
def calculate():


def calculate(tokens):
    result = tokens[0]
    for i in range(0, len(tokens)):
        if '*' in tokens:
            result = tokens[tokens.index('*') - 1] * tokens[tokens.index('*') + 1]
        elif '/' in tokens:
            result = tokens[tokens.index('/') - 1] / tokens[tokens.index('/') + 1]
        else:
            if tokens[i] == '+':
                result = result + tokens[i+1]
            elif tokens[i] == '-':
                result = result - tokens[i+1]

    print(result)
    return result
calculate(tokenize("два плюс пять разделить пять"))
