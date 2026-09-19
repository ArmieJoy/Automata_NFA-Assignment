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


# --- DFA Configuration from the Minimized Whiteboard Transition Table ---
states = {'AC', 'B', 'D', 'E'} 
alphabet = {'0', '1'}

transitions = {
    'AC': {'0': 'B', '1': 'AC'}, 
    'B':  {'0': 'B', '1': 'D'},  
    'D':  {'0': 'B', '1': 'E'},  
    'E':  {'0': 'B', '1': 'AC'}  
}

start_state = 'AC'
accept_states = {'E'} 

dfa = DFA(states, alphabet, transitions, start_state, accept_states)


# --- PART 1: AUTOMATED PRE-SET TESTS (Short & Long Inputs) ---
print("=" * 75)
print("              PART 1: AUTOMATED EXTENDED TEST SUITE             ")
print("=" * 75)

test_inputs = [
    # Whiteboard examples
    "0110",        # Rejected
    "011011",      # Accepted
    
    # Short & Long Accepted
    "011",         # AC -> B -> D -> E
    "00011",       # AC -> B -> B -> B -> D -> E
    "1011",        # AC -> AC -> B -> D -> E
    "111011",      # Loop AC on ones, then B -> D -> E
    "0111011",     # AC -> B -> D -> E -> AC -> B -> D -> E
    
    # Short & Long Rejected
    "",            # Start state AC
    "1",           # Ends at AC
    "0",           # Ends at B
    "01",          # Ends at D
    "01100",       # Ends at B
    "00000",       # Ends at B
    "11111",       # Ends at AC
    "011010"       # Ends at B
]

print(f"{'Input String':<15} | {'Status':<10} | State Transition Path")
print("-" * 75)

for inp in test_inputs:
    accepted, path, status = dfa.process_string(inp)
    formatted_input = f"'{inp}'" if inp else "'' (empty)"
    path_str = " -> ".join(path)
    print(f"{formatted_input:<15} | {status:<10} | {path_str}")


# --- PART 2: SINGLE CUSTOM USER INPUT ---
print("\n" + "=" * 75)
print("              PART 2: SINGLE CUSTOM INPUT TEST               ")
print("=" * 75)

user_input = input("Enter binary string to test: ").strip()

accepted, path, status = dfa.process_string(user_input)

if type(accepted) == bool: # Quick check to bypass invalid input string error messages breaking the join
    path_str = " -> ".join(path)
else:
    path_str = "N/A"
    
formatted_input = f"'{user_input}'" if user_input else "'' (empty string)"

print("\n" + "-" * 75)
print(f"Input       : {formatted_input}")
print(f"Path        : {path_str}")
print(f"Result      : {status}")
print("-" * 75)
print("Program completed.")