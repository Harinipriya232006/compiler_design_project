"""Simple code generator that emits pseudo assembly from intermediate code."""


def generate_code(quads):
    assembly = []
    for op, arg1, arg2, result in quads:
        if op == '+':
            assembly.append(f'MOV R1, {arg1}')
            assembly.append(f'ADD R1, {arg2}')
            assembly.append(f'MOV {result}, R1')
        elif op == '-':
            assembly.append(f'MOV R1, {arg1}')
            assembly.append(f'SUB R1, {arg2}')
            assembly.append(f'MOV {result}, R1')
        elif op == '*':
            assembly.append(f'MOV R1, {arg1}')
            assembly.append(f'MUL R1, {arg2}')
            assembly.append(f'MOV {result}, R1')
        elif op == '/':
            assembly.append(f'MOV R1, {arg1}')
            assembly.append(f'DIV R1, {arg2}')
            assembly.append(f'MOV {result}, R1')
        else:
            assembly.append(f'; unsupported op {op}')
    return assembly


def main():
    quads = [
        ('+', 'a', 'b', 't1'),
        ('*', 't1', 'c', 't2'),
        ('-', 't2', 'd', 't3')
    ]
    code = generate_code(quads)
    print('Generated pseudo-assembly:')
    for line in code:
        print(' ', line)


if __name__ == '__main__':
    main()
