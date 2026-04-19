"""Global data flow analysis example: live variable analysis."""


def analyze_live_variables(blocks, successors):
    live_in = {block: set() for block in blocks}
    live_out = {block: set() for block in blocks}
    changed = True

    while changed:
        changed = False
        for block in reversed(blocks):
            out_set = set()
            for succ in successors.get(block, []):
                out_set |= live_in[succ]

            in_set = out_set.copy()
            for var in reversed(blocks[block]['defs']):
                if var in in_set:
                    in_set.remove(var)
            in_set |= set(blocks[block]['uses'])

            if live_out[block] != out_set or live_in[block] != in_set:
                live_out[block] = out_set
                live_in[block] = in_set
                changed = True

    return live_in, live_out


def main():
    blocks = {
        'B1': {'defs': ['a'], 'uses': ['b', 'c']},
        'B2': {'defs': ['b'], 'uses': ['a']},
        'B3': {'defs': ['c'], 'uses': ['b']}
    }
    successors = {'B1': ['B2', 'B3'], 'B2': ['B3'], 'B3': []}

    live_in, live_out = analyze_live_variables(blocks, successors)
    print('Live variable analysis results:')
    for blk in blocks:
        print(f'  {blk}: IN={sorted(live_in[blk])}, OUT={sorted(live_out[blk])}')


if __name__ == '__main__':
    main()
