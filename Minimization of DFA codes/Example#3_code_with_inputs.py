def simulate_minimized_dfa(input_string):
    # Define the transition table based on the minimized graph in the image
    transitions = {
        'a':  {'0': 'bc', '1': 'bc'},
        'bc': {'0': 'bc', '1': 'de'},
        'de': {'0': 'de', '1': 'f'},
        'f':  {'0': 'f',  '1': 'f'}
    }
    
    start_state = 'a'
    accept_states = {'de'} # 'de' is the only accept state
    
    current_state = start_state
    path = [current_state] # Keep track of the states visited
    
    # Process each character in the input string
    for char in input_string:
        if char not in ['0', '1']:
            return f"Error: Invalid character '{char}'. Please enter only 0s and 1s."
        
        # Move to the next state
        current_state = transitions[current_state][char]
        path.append(current_state) # Record the new state in the path
        
    # Format the path list into a readable string with arrows
    path_str = " -> ".join(path)
        
    # Check if the final state is an accept state and return result with path
    if current_state in accept_states:
        return f"Accepted (✓)\n    Path: {path_str}"
    else:
        return f"Rejected (✗)\n    Path: {path_str}"

if __name__ == "__main__":
    print("--- Minimized DFA Simulator ---")
    
    # Expanded lists of built-in examples
    examples_accepted = [
        "001",       # From notes
        "100100",    # From notes
        "01",        # Short accepted
        "110",       # Accepted with trailing zero
        "0000001"    # Long accepted
    ]
    
    examples_rejected = [
        "1011",      # From notes
        "100110",    # From notes
        "0",         # Too short, ends at 'bc'
        "000",       # No 1s to trigger the jump to 'de', ends at 'bc'
        "011"        # Too many 1s, pushes to dead state 'f'
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