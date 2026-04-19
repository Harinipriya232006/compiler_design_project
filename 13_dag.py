"""Directed Acyclic Graph (DAG) construction for expression optimization."""


def build_dag(expressions):
    nodes = {}
    edges = {}

    def make_node(op, left, right):
        key = (op, left, right)
        if key not in nodes:
            index = len(nodes) + 1
            nodes[key] = f'N{index}'
            edges[nodes[key]] = (op, left, right)
        return nodes[key]

    for expr in expressions:
        op, left, right = expr
        left_node = left
        right_node = right
        if isinstance(left, tuple):
            left_node = make_node(*left)
        if isinstance(right, tuple):
            right_node = make_node(*right)
        make_node(op, left_node, right_node)

    return nodes, edges


def main():
    expressions = [
        ('+', 'a', 'b'),
        ('*', ('+', 'a', 'b'), 'c'),
        ('+', 'a', 'b')
    ]

    nodes, edges = build_dag(expressions)
    print('DAG nodes:')
    for key, name in nodes.items():
        print(' ', name, '=', key)

    print('\nDAG edges:')
    for node, detail in edges.items():
        op, left, right = detail
        print(f'  {node}: {left} {op} {right}')


if __name__ == '__main__':
    main()
