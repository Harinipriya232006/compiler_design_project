"""Predictive parsing / LL(1) parsing example."""

def compute_first(productions):
    first = {nt: set() for nt in productions}
    changed = True

    while changed:
        changed = False
        for nt, rules in productions.items():
            for rule in rules:
                if rule == ['ε']:
                    if 'ε' not in first[nt]:
                        first[nt].add('ε')
                        changed = True
                else:
                    for symbol in rule:
                        if symbol.isupper():
                            before = len(first[nt])
                            first[nt] |= {x for x in first[symbol] if x != 'ε'}
                            if 'ε' not in first[symbol]:
                                break
                            if len(first[nt]) != before:
                                changed = True
                        else:
                            if symbol not in first[nt]:
                                first[nt].add(symbol)
                                changed = True
                            break
    return first


def compute_follow(productions, first, start_symbol):
    follow = {nt: set() for nt in productions}
    follow[start_symbol].add('$')
    changed = True

    while changed:
        changed = False
        for nt, rules in productions.items():
            for rule in rules:
                trailer = follow[nt].copy()
                for symbol in reversed(rule):
                    if symbol.isupper():
                        before = len(follow[symbol])
                        follow[symbol] |= trailer
                        if 'ε' in first[symbol]:
                            trailer |= {x for x in first[symbol] if x != 'ε'}
                        else:
                            trailer = {x for x in first[symbol] if x != 'ε'}
                        if len(follow[symbol]) != before:
                            changed = True
                    else:
                        trailer = {symbol}
    return follow


def main():
    productions = {
        'E': [['T', 'E\'']],
        'E\'': [['+', 'T', 'E\''], ['ε']],
        'T': [['F', 'T\'']],
        'T\'': [['*', 'F', 'T\''], ['ε']],
        'F': [['(', 'E', ')'], ['id']]
    }

    first = compute_first(productions)
    follow = compute_follow(productions, first, 'E')

    print('FIRST sets:')
    for nt, values in first.items():
        print(f'  {nt} =', sorted(values))

    print('\nFOLLOW sets:')
    for nt, values in follow.items():
        print(f'  {nt} =', sorted(values))


if __name__ == '__main__':
    main()
