def nfa_to_dfa(nfa_trans, start, accept):
    dfa_states = []
    dfa_trans = {}
    dfa_accept = []
    queue = [frozenset([start])]
    state_map = {frozenset([start]): 0}
    dfa_states.append(frozenset([start]))
    if start in accept:
        dfa_accept.append(0)
    while queue:
        current = queue.pop(0)
        state_id = state_map[current]
        for symbol in nfa_trans[start].keys():  # assume all have same
            next_set = set()
            for state in current:
                if state in nfa_trans and symbol in nfa_trans[state]:
                    next_set.update(nfa_trans[state][symbol])
            next_set.discard(-1)  # remove -1
            if next_set:
                next_froz = frozenset(next_set)
                if next_froz not in state_map:
                    state_map[next_froz] = len(dfa_states)
                    dfa_states.append(next_froz)
                    queue.append(next_froz)
                    if any(s in accept for s in next_set):
                        dfa_accept.append(len(dfa_states) - 1)
                dfa_trans[(state_id, symbol)] = state_map[next_froz]
    return dfa_states, dfa_trans, dfa_accept

if __name__ == "__main__":
    with open("inputs/input_nfa.txt", "r") as f:
        lines = f.readlines()
    num_states = int(lines[0].strip())
    alphabet = lines[1].strip().split()
    nfa_trans = {i: {} for i in range(num_states)}
    idx = 2
    for i in range(num_states):
        for sym in alphabet:
            next_states = [int(x) for x in lines[idx].strip().split() if x != '-1']
            nfa_trans[i][sym] = next_states
            idx += 1
    start = int(lines[idx].strip())
    accept = [int(x) for x in lines[idx+1].strip().split()]
    dfa_states, dfa_trans, dfa_accept = nfa_to_dfa(nfa_trans, start, accept)
    with open("outputs/output_dfa.txt", "w") as f:
        f.write(f"DFA States: {len(dfa_states)}\n")
        f.write(f"Alphabet: {' '.join(alphabet)}\n")
        f.write("Transitions:\n")
        for (s, sym), ns in dfa_trans.items():
            f.write(f"{s} --{sym}--> {ns}\n")
        f.write(f"Start: 0\n")
        f.write(f"Accept: {' '.join(map(str, dfa_accept))}\n")
    print("NFA to DFA conversion complete. Check outputs/output_dfa.txt")