def simulate_minimized_dfa(input_string):
    # Define the transition table based on the minimized graph in Example #4
    transitions = {
        'ABFG': {'0': 'ABFG', '1': 'CD'},
        'CD':   {'0': 'E',    '1': 'ABFG'},
        'E':    {'0': 'E',    '1': 'E'}
    }
    
    start_state = 'ABFG'
    accept_states = {'CD'} # 'CD' is the final/accept state
    
    current_state = start_state
    path = [current_state] 
    
    # Process each character in the input string
    for char in input_string:
        if char not in ['0', '1']:
            return f"Error: Invalid character '{char}'. Please enter only 0s and 1s."
        
        # Move to the next state
        current_state = transitions[current_state][char]
        path.append(current_state) 
        
    # Format the path list into a readable string with arrows
    path_str = " -> ".join(path)
        
    # Check if the final state is an accept state and return result with path
    if current_state in accept_states:
        return f"Accepted (✓)\n    Path: {path_str}"
    else:
        return f"Rejected (✗)\n    Path: {path_str}"

if __name__ == "__main__":
    print("--- Minimized DFA Simulator (Example #4) ---")
    
    # Expanded lists of built-in examples
    examples_accepted = [
        "1101",      # From notes
        "01101",     # From notes
        "1",         # Short accepted string
        "0001",      # Leading zeros
        "111"        # Odd number of 1s
    ]
    
    examples_rejected = [
        "00110",     # From notes
        "0100",      # From notes
        "0",         # Ends at start state 'ABFG'
        "10",        # Triggers the dead state 'E'
        "11"         # Ends back at start state 'ABFG'
    ]
    
    print("Testing built-in ACCEPTED examples...")
    for ex in examples_accepted:
        print(f"  String '{ex}':\n    {simulate_minimized_dfa(ex)}")
        
    print("\nTesting built-in REJECTED examples...")
    for ex in examples_rejected:
        print(f"  String '{ex}':\n    {simulate_minimized_dfa(ex)}")
    print("-------------------------------\n")
    
    # Ask the user for input exactly once
    user_input = input("Now it's your turn! Enter a binary string (0s and 1s): ").strip()
    
    if user_input:
        result = simulate_minimized_dfa(user_input)
        print(f"\nResult for your string '{user_input}':\n    {result}")
    else:
        print("\nNo input provided.")