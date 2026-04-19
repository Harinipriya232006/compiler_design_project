"""Computation of LEADING and TRAILING sets for grammar symbols."""


def compute_leading(productions):
    leading = {nt: set() for nt in productions}
    changed = True

    while changed:
        changed = False
        for nt, rules in productions.items():
            for rule in rules:
                first = rule[0]
                if first.islower() or first in ['(', ')', '+', '*', 'id']:
                    if first not in leading[nt]:
                        leading[nt].add(first)
                        changed = True
                else:
                    if first not in leading[nt]:
                        leading[nt] |= leading[first]
                        changed = True
    return leading


def compute_trailing(productions):
    trailing = {nt: set() for nt in productions}
    changed = True

    while changed:
        changed = False
        for nt, rules in productions.items():
            for rule in rules:
                last = rule[-1]
                if last.islower() or last in ['(', ')', '+', '*', 'id']:
                    if last not in trailing[nt]:
                        trailing[nt].add(last)
                        changed = True
                else:
                    if last not in trailing[nt]:
                        trailing[nt] |= trailing[last]
                        changed = True
    return trailing


def main():
    productions = {
        'E': [['T', 'E\'']],
        'E\'': [['+', 'T', 'E\''], ['ε']],
        'T': [['F', 'T\'']],
        'T\'': [['*', 'F', 'T\''], ['ε']],
        'F': [['(', 'E', ')'], ['id']]
    }

    print('LEADING sets:')
    for nt, vals in compute_leading(productions).items():
        print(f'  {nt} =', sorted(vals))

    print('\nTRAILING sets:')
    for nt, vals in compute_trailing(productions).items():
        print(f'  {nt} =', sorted(vals))


if __name__ == '__main__':
    main()
