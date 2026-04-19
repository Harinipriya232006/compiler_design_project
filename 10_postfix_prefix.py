"""Convert infix expressions to postfix and prefix form."""

precedence = {
    '+': 1,
    '-': 1,
    '*': 2,
    '/': 2,
    '^': 3
}


def is_operator(token):
    return token in precedence


def infix_to_postfix(expression):
    stack = []
    output = []
    tokens = expression.split()

    for token in tokens:
        if token.isalnum():
            output.append(token)
        elif token == '(':
            stack.append(token)
        elif token == ')':
            while stack and stack[-1] != '(':
                output.append(stack.pop())
            stack.pop()
        else:
            while stack and stack[-1] != '(' and precedence.get(stack[-1], 0) >= precedence[token]:
                output.append(stack.pop())
            stack.append(token)

    while stack:
        output.append(stack.pop())

    return ' '.join(output)


def infix_to_prefix(expression):
    tokens = expression.split()[::-1]
    tokens = ['(' if token == ')' else ')' if token == '(' else token for token in tokens]
    reversed_expr = ' '.join(tokens)
    postfix = infix_to_postfix(reversed_expr)
    return ' '.join(postfix.split()[::-1])


def main():
    expr = 'a + b * ( c - d )'
    print('Infix:', expr)
    print('Postfix:', infix_to_postfix(expr))
    print('Prefix:', infix_to_prefix(expr))


if __name__ == '__main__':
    main()
