"""Shift-reduce parser demo for a small grammar."""

from collections import deque


grammar = {
    'E': [['E', '+', 'T'], ['T']],
    'T': [['T', '*', 'F'], ['F']],
    'F': [['(', 'E', ')'], ['id']]
}

reductions = {
    ('E', '+', 'T'): 'E',
    ('T', '*', 'F'): 'T',
    ('(', 'E', ')'): 'F',
    ('id',): 'F',
    ('F',): 'T',
    ('T',): 'E'
}


def shift_reduce_parse(tokens):
    stack = deque()
    input_tokens = deque(tokens + ['$'])
    actions = []

    while True:
        made_reduction = False
        for size in range(len(stack), 0, -1):
            substring = tuple(list(stack)[-size:])
            if substring in reductions:
                stack_size_before = len(stack)
                for _ in range(size):
                    stack.pop()
                stack.append(reductions[substring])
                actions.append(f'reduce {substring} -> {reductions[substring]}')
                made_reduction = True
                break

        if not made_reduction:
            if input_tokens[0] == '$' and list(stack) == ['E']:
                actions.append('accept')
                break
            symbol = input_tokens.popleft()
            stack.append(symbol)
            actions.append(f'shift {symbol}')
            if symbol == '$' and list(stack) != ['E']:
                actions.append('reject')
                break

    return actions


def main():
    tokens = ['id', '+', 'id', '*', 'id']
    result = shift_reduce_parse(tokens)
    print('Input:', ' '.join(tokens))
    print('\nActions:')
    for action in result:
        print(' ', action)


if __name__ == '__main__':
    main()
