class DFA:
    def __init__(self, states, alphabet, transitions, start_state, accept_states):
        self.states = states
        self.alphabet = alphabet
        self.transitions = transitions
        self.start_state = start_state
        self.accept_states = accept_states

    def process_string(self, input_string):
        current_state = self.start_state
        path = [current_state]
        
        for symbol in input_string:
            if symbol not in self.alphabet:
                return False, path, f"Invalid symbol '{symbol}' (Only 0 and 1 allowed)"
            
            current_state = self.transitions[current_state][symbol]
            path.append(current_state)
            
        is_accepted = current_state in self.accept_states
        return is_accepted, path, "ACCEPTED" if is_accepted else "REJECTED"


# --- DFA Configuration (MINIMIZED Version) ---
# Original states {A, B} are combined into 'AB'
# Original states {C, D, E} are combined into 'CDE'
# Original state {F} remains 'F'

states = {'AB', 'CDE', 'F'}
alphabet = {'0', '1'}

transitions = {
    'AB':  {'0': 'AB',  '1': 'CDE'},
    'CDE': {'0': 'CDE', '1': 'F'},
    'F':   {'0': 'F',   '1': 'F'}
}

start_state = 'AB'
accept_states = {'CDE'}

dfa = DFA(states, alphabet, transitions, start_state, accept_states)


# --- PART 1: AUTOMATED PRE-SET TESTS (Short & Long Inputs) ---
print("=" * 65)
print("              PART 1: AUTOMATED EXTENDED TEST SUITE             ")
print("=" * 65)

test_inputs = [
    # Short & Long Accepted
    "1", "01", "001", "00001", "00000001", "010", "0010", "0000100",
    # Short & Long Rejected
    "", "0", "00", "11", "000", "00000", "101", "0101", "000011100"
]

print(f"{'Input String':<15} | {'Status':<10} | State Transition Path")
print("-" * 65)

for inp in test_inputs:
    accepted, path, status = dfa.process_string(inp)
    formatted_input = f"'{inp}'" if inp else "'' (empty)"
    path_str = " -> ".join(path)
    print(f"{formatted_input:<15} | {status:<10} | {path_str}")


# --- PART 2: SINGLE CUSTOM USER INPUT ---
print("\n" + "=" * 65)
print("              PART 2: SINGLE CUSTOM INPUT TEST               ")
print("=" * 65)

user_input = input("Enter binary string to test: ").strip()

accepted, path, status = dfa.process_string(user_input)

path_str = " -> ".join(path)
formatted_input = f"'{user_input}'" if user_input else "'' (empty string)"

print("\n" + "-" * 55)
print(f"Input       : {formatted_input}")
print(f"Path        : {path_str}")
print(f"Result      : {status}")
print("-" * 55)
print("Program completed.")