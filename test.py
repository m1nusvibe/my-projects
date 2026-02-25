while '*' in tokens or '/' in tokens:
    if '*' in tokens:
        idx = tokens.index('*')
        a, _, b = tokens[idx - 1: idx + 2]
        result = a * b
        tokens[idx - 1] = result
        del tokens[idx:idx + 2]
    elif '/' in tokens:
        idx = tokens.index('/')
        a, _, b = tokens[idx - 1:idx + 2]
        result = a / b
        tokens[idx - 1] = result
        del tokens[idx:idx + 2]

while '+' in tokens or '-' in tokens:
    if '+' in tokens:
        idx = tokens.index('+')
        a, _, b = tokens[idx - 1:idx + 2]
        result = a + b
        tokens[idx - 1] = result
        del tokens[idx:idx + 2]

    elif '-' in tokens:
        idx = tokens.index('-')
        a, _, b = tokens[idx - 1:idx + 2]
        result = a - b
        tokens[idx - 1] = result
        del tokens[idx:idx + 2]

print(tokens[0])
return tokens[0]