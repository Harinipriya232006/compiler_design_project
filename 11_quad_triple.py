"""Generate quadruple, triple, and indirect triple representations."""


def generate_quads(expressions):
    quads = []
    temp_id = 1
    for expr in expressions:
        result = f't{temp_id}'
        op, arg1, arg2 = expr
        quads.append((op, arg1, arg2, result))
        temp_id += 1
    return quads


def generate_triples(quads):
    triples = []
    for i, (op, arg1, arg2, result) in enumerate(quads):
        triples.append((op, arg1, arg2))
    return triples


def generate_indirect_triples(triples):
    indirect = [(i, triple) for i, triple in enumerate(triples)]
    return indirect


def main():
    expressions = [
        ('+', 'a', 'b'),
        ('*', 't1', 'c')
    ]

    quads = generate_quads(expressions)
    triples = generate_triples(quads)
    indirect = generate_indirect_triples(triples)

    print('Quadruples:')
    for item in quads:
        print(' ', item)

    print('\nTriples:')
    for item in triples:
        print(' ', item)

    print('\nIndirect triples:')
    for item in indirect:
        print(' ', item)


if __name__ == '__main__':
    main()
