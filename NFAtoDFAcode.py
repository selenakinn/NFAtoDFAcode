import copy

def nfa_to_dfa(nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_final_states):
    dfa_states = set()
    dfa_alphabet = nfa_alphabet
    dfa_transitions = {}
    dfa_start_state = frozenset([nfa_start_state])
    dfa_final_states = set()

    queue = [dfa_start_state]
    dfa_states.add(dfa_start_state)

    while queue:
        current_state = queue.pop(0)
        for symbol in dfa_alphabet:
            next_state = set()
            for state in current_state:
                if (state, symbol) in nfa_transitions:
                    next_state.update(nfa_transitions[(state, symbol)])
            next_state = frozenset(next_state)
            if next_state not in dfa_states:
                dfa_states.add(next_state)
                queue.append(next_state)
            if next_state not in dfa_transitions:
                dfa_transitions[next_state] = {}
            dfa_transitions[next_state][symbol] = next_state

    for state in dfa_states:
        if any(s in nfa_final_states for s in state):
            dfa_final_states.add(state)

    return dfa_states, dfa_alphabet, dfa_transitions, dfa_start_state, dfa_final_states

# Get input from the user
num_states = int(input("Enter the number of states in the NFA: "))
nfa_states = [f"q{i}" for i in range(num_states)]

nfa_alphabet = input("Enter the alphabet (space-separated): ").split()

nfa_transitions = {}
print("Enter the transitions (state symbol state):")
while True:
    transition = input().strip()
    if not transition:
        break
    parts = transition.split()
    state, symbol, next_state = parts[0], parts[1], parts[2]
    nfa_transitions[(state, symbol)] = [next_state]

nfa_start_state = input("Enter the start state: ")
nfa_final_states = input("Enter the final states (space-separated): ").split()

dfa_states, dfa_alphabet, dfa_transitions, dfa_start_state, dfa_final_states = nfa_to_dfa(
    nfa_states, nfa_alphabet, nfa_transitions, nfa_start_state, nfa_final_states
)

print("DFA Alphabet:", dfa_alphabet)
print("DFA Transitions:", dfa_transitions)
print("DFA Initial State:", dfa_start_state)
print("Final DFA states:")
for state in dfa_final_states:
    print(dfa_final_states)