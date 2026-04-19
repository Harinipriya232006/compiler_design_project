"""Construction of LR(0) items for a grammar."""


def closure(items, productions):
    closure_set = set(items)
    changed = True

    while changed:
        changed = False
        for item in list(closure_set):
            lhs, rhs, dot = item
            if dot < len(rhs):
                symbol = rhs[dot]
                if symbol.isupper():
                    for prod in productions[symbol]:
                        new_item = (symbol, prod, 0)
                        if new_item not in closure_set:
                            closure_set.add(new_item)
                            changed = True
    return closure_set


def goto(items, symbol, productions):
    moved = set()
    for lhs, rhs, dot in items:
        if dot < len(rhs) and rhs[dot] == symbol:
            moved.add((lhs, rhs, dot + 1))
    return closure(moved, productions)


def main():
    productions = {
        'S': [['E']],
        'E': [['E', '+', 'T'], ['T']],
        'T': [['T', '*', 'F'], ['F']],
        'F': [['(', 'E', ')'], ['id']]
    }
    start_item = ('S', productions['S'][0], 0)
    item_set = closure({start_item}, productions)
    print('LR(0) Closure for S -> .E')
    for item in sorted(item_set):
        lhs, rhs, dot = item
        rhs_str = ' '.join(rhs[:dot] + ['.'] + rhs[dot:])
        print(f'  {lhs} -> {rhs_str}')

    state = goto(item_set, 'E', productions)
    print('\nGOTO(I0, E):')
    for item in sorted(state):
        lhs, rhs, dot = item
        rhs_str = ' '.join(rhs[:dot] + ['.'] + rhs[dot:])
        print(f'  {lhs} -> {rhs_str}')


if __name__ == '__main__':
    main()
