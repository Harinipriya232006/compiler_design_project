"""Simple storage allocation strategy example using stack allocation."""


def allocate_stack(variables):
    offset = 0
    allocation = {}
    for var in variables:
        allocation[var] = offset
        offset += 4  # each variable gets 4 bytes on stack
    return allocation


def main():
    variables = ['x', 'y', 'z', 'temp']
    allocation = allocate_stack(variables)
    print('Stack allocation offsets:')
    for var, offset in allocation.items():
        print(f'  {var}: [BP{offset:+}]')


if __name__ == '__main__':
    main()
