
Practical 1 

Aim:Design a Program for creating machine that accepts the string always ending with 101. 

Code: 

class StateMachine: 
    def __init__(self): 
        self.state = 'q0' 
    def process_input(self, input_string): 
        for symbol in input_string: 
            if self.state == 'q0' and symbol == '1': 
                self.state = 'q1' 
            elif self.state == 'q0' and symbol == '0': 
                self.state = 'q0' 
            elif self.state == 'q1' and symbol == '1': 
                self.state = 'q0' 
            elif self.state == 'q1' and symbol == '0': 
                self.state = 'q2' 
            elif self.state == 'q2' and symbol == '1': 
                self.state = 'q3' 
            elif self.state == 'q2' and symbol == '0': 
                self.state = 'q0' 
            elif self.state == 'q3' and symbol == '1': 
                self.state = 'q4' 
            elif self.state == 'q3' and symbol == '0': 
                self.state = 'q4' 
            elif self.state == 'q4' and symbol == '1': 
                self.state = 'q4' 
            elif self.state == 'q4' and symbol == '0': 
                self.state = 'q4' 
            else: 
                self.state = 'q0' 
        # Check the final state 

        return self.state == 'q3' 
def main(): 
    input_string = input("Enter a string of 0s and 1s: ") 
    fsm = StateMachine() 
    result = fsm.process_input(input_string) 
    if result: 
        print("Accepted! The string always ends with '101'.") 
    else: 
        print("Rejected! The string does not end with '101'.") 
if __name__ == "__main__": 
    main() 

 

Output: 

Enter a string of 0s and 1s: 00101 

Accepted! The string always ends with '101'. 











 

Practical 2 

Aim: 

Design a Program for creating machine that accepts three consecutive one. 

Code: 

class StateMachine: 
    def __init__(self): 
        self.state = 'q0' 
        self.consecutive_ones = 0 
    def process_input(self, input_string): 
        for symbol in input_string: 
            if self.state == 'q0' and symbol == '1': 
                self.consecutive_ones = 1 
                self.state = 'q1' 
            elif self.state == 'q1' and symbol == '1': 
                self.consecutive_ones += 1 
                if self.consecutive_ones == 3: 
                    self.state = 'q2' 
            else: 
                self.consecutive_ones = 0 
                self.state = 'q0' 
        # Check the final state 
        return self.state == 'q2' 
def main(): 
    input_string = input("Enter a string of 0s and 1s: ") 
    fsm = StateMachine() 
    result = fsm.process_input(input_string) 
    if result: 
        print("Accepted! The string contains three consecutive '1's.") 
    else: 
        print("Rejected! The string does not contain three consecutive '1's.") 
if __name__ == "__main__": 
    main() 

 

Output: 

Enter a string of 0s and 1s: 00111 

Accepted! The string contains three consecutive '1's. 

 











Practical – 3 

Aim: 

Design a program for accepting decimal number divisible by 2. 

Code: 
class StateMachine: 
    def __init__(self): 
        self.state = 'q0' 
    def process_input(self, input_string): 
        for digit in input_string: 
            if self.state == 'q0': 
                self.state = 'q1' if digit == '0' or digit == '2' or digit == '4' or digit == '6' or digit == '8' else 'q0' 
            elif self.state == 'q1': 
                self.state = 'q0' if digit.isdigit() else 'q0' 
        # Check the final state 
        return self.state == 'q1' 
def main(): 
    input_string = input("Enter a decimal number: ") 
    fsm = StateMachine() 
    result = fsm.process_input(input_string) 
    if result: 
        print("Accepted! The decimal number is divisible by 2.") 
    else: 
        print("Rejected! The decimal number is not divisible by 2.") 
if __name__ == "__main__": 
    main() 

 

Output:[Text Wrapping Break]Enter a decimal number: 4.0 

Accepted! The decimal number is divisible by 2. 

 












Practical – 4 

Aim: 

Design a program for creating a machine which accepts string having equal no. of 1’s and 0’s. 

Code: 
class StateMachine: 
    def __init__(self): 
        self.state = 'q0' 
    def process_input(self, input_string): 
        for symbol in input_string: 
            if self.state == 'q0' and symbol == '0': 
                self.state = 'q1' 
            elif self.state == 'q0' and symbol == '1': 
                self.state = 'q2' 
            elif self.state == 'q1' and symbol == '0': 
                self.state = 'q0' 
            elif self.state == 'q1' and symbol == '1': 
                self.state = 'q3' 
            elif self.state == 'q2' and symbol == '0': 
                self.state = 'q3' 
            elif self.state == 'q2' and symbol == '1': 
                self.state = 'q0' 
            elif self.state == 'q3' and symbol == '0': 
                self.state = 'q2' 
            elif self.state == 'q3' and symbol == '1': 
                self.state = 'q1' 
        # Check the final state 
        return self.state == 'q0' 
def main(): 
    input_string = input("Enter a string of 1s and 0s: ") 
    fsm = StateMachine() 
    result = fsm.process_input(input_string) 
    if result: 
        print("Accepted! The string has an equal number of 1s and 0s.") 
    else: 
        print("Rejected! The string does not have an equal number of 1s and 0s.") 
if __name__ == "__main__": 

    main() 

 

Output: 

Enter a string of 1s and 0s: 0011 

Accepted! The string has an equal number of 1s and 0s. 

 













Practical – 5 

Aim: 

Design a program for creating a machine which count number of 1’s and 0’s in a given string. 

Code: 

class CountMachine: 
    def __init__(self): 
        self.state = "start" 
        self.count_0 = 0 
        self.count_1 = 0 
    def transition(self, char): 
        if self.state == "start": 
            if char == '0': 
                self.count_0 += 1 
            elif char == '1': 
                self.count_1 += 1 
            else: 
                raise ValueError("Invalid input character") 
        else: 
            raise ValueError("Invalid state") 
    def process_input(self, input_str): 
        for char in input_str: 
            self.transition(char) 
    def get_counts(self): 
        return self.count_0, self.count_1 
def main(): 
    input_str = input("Enter a string containing 1's and 0's: ") 
    machine = CountMachine() 
    machine.process_input(input_str) 
    count_0, count_1 = machine.get_counts() 
    print("Number of 0's:", count_0) 
    print("Number of 1's:", count_1) 
if __name__ == "__main__": 

    main() 

 

Output: 

Enter a string containing 1's and 0's: 1010 

Number of 0's: 2 

Number of 1's: 2 
























 

Practical – 6 

Aim: 

Write a program for tokenization of given input. 

Code:[Text Wrapping Break]
def tokenize(input_string): 
    tokens = [] 
    current_word = "" 
    state = "start" 
    for char in input_string: 
        if state == "start": 
            if char != " ":  # Start of a new word 
                current_word += char 
                state = "in_word" 
        elif state == "in_word": 
            if char != " ":  # Continue adding characters to the current word 
                current_word += char 
            else:  # End of the current word, append it to tokens 
                tokens.append(current_word) 
                current_word = "" 
                state = "start" 
    if current_word:  # Append the last word if it exists 
        tokens.append(current_word) 
    return tokens 
# Test the tokenizer 
input_string = "Tokenization of given input" 
tokens = tokenize(input_string) 
print(tokens) 

 


Output:[Text Wrapping Break]['This', 'is', 'a', 'sample', 'input', 'string.'] 












 

Practical – 7 

Aim: 

Write a program for generating regular expressions for regular grammar 

Code:[Text Wrapping Break]
class RegularGrammar:
    def __init__(self): 
        self.productions = {} 
    def add_production(self, non_terminal, expression): 
        if non_terminal in self.productions: 
            self.productions[non_terminal].append(expression) 
        else: 
            self.productions[non_terminal] = [expression] 
    def generate_regex(self, non_terminal): 
        if non_terminal not in self.productions: 
            return None 
        regex = "|".join(self.productions[non_terminal]) 
        if len(self.productions[non_terminal]) > 1: 
            regex = f"({regex})"
        return regex 
if __name__ == "__main__": 
    grammar = RegularGrammar() 
    # Example regular grammar rules 
    grammar.add_production("S", "a") 
    grammar.add_production("S", "bS") 
    grammar.add_production("S", "") 
    # Generating regular expressions for each non-terminal 
    for non_terminal in grammar.productions: 
        regex = grammar.generate_regex(non_terminal) 
        print(f"Regex for {non_terminal}: {regex}") 

 

Output:[Text Wrapping Break]Regex for S: (a|bS|) 

 













Practical 8 

Aim: 

Write a program for generating derivation sequence / language for the given sequence of productions 

Code: 

def generate_derivation(grammar, start_symbol, max_depth): 
    # Define a recursive function to derive sequences 
    def derive(sentence, depth): 
        # If the maximum depth is reached, return the current sentence 
        if depth >= max_depth: 
            return [sentence] 
        derivations = [] 
        # Iterate over each symbol in the sentence 
        for i, symbol in enumerate(sentence): 
            # Check if the symbol has production rules defined 
            if symbol in grammar: 
                # Apply each production rule to the symbol 
                for production in grammar[symbol]: 
                    # Create a new sentence by replacing the symbol with the production 
                    new_sentence = sentence[:i] + production + sentence[i+1:] 
                    # Recursively derive sequences from the new sentence 
                    derivations.extend(derive(new_sentence, depth + 1)) 
        return derivations 
    # Start the derivation process with the start symbol and depth 0 
    return derive(start_symbol, 0) 
# Test the function 
grammar = { 
    'S': ['AB', 'BC'], 
    'A': ['a'], 
    'B': ['b'], 
    'C': ['c'] 
} 
start_symbol = 'S' 
max_depth = 3 
derivation_sequence = generate_derivation(grammar, start_symbol, max_depth) 
# Print the generated derivation sequence/language 
print("Derivation sequence / Language:") 
for derivation in derivation_sequence: 
    print(derivation) 

 

Output: 

Derivation sequence / Language: 

ab 

ab 

bc 

bc 













 

Practical 9 

Aim:  

Design a Turing machine to recognize all strings consisting of an even number of 1's. 

Code: 

states = { 
    'A': { 
        '0': ('A', '0', 'R'), 
        '1': ('B', '0', 'R'), 
        '_': ('C', '_', 'L') 
    }, 
    'B': { 
        '0': ('B', '0', 'R'), 
        '1': ('A', '0', 'R'), 
        '_': ('C', '_', 'L') 
    }, 
    'C': {} 
} 
initial_state = "A" 
final_state = {"A"} 
def turing_machine(input_str): 
    current_state = initial_state 
    tape = list(input_str) 
    i_head = 0 
    while True: 
        if tape[i_head] not in states[current_state]: 
            return False 
        new_state, write_value, move_dir = states[current_state][tape[i_head]] 
        tape[i_head] = write_value 
        if move_dir == 'R': 
            i_head += 1 
        elif move_dir == 'L': 
            i_head -= 1 
        current_state = new_state 
        if current_state in final_state and i_head >= len(tape): 
            return True 
        elif current_state not in states or i_head >= len(tape) or i_head < 0: 
            return False 
print(turing_machine('011'))       # True 
print(turing_machine('01111'))     # True 
print(turing_machine('010101111')) # True 
print(turing_machine('01'))        # False 
print(turing_machine('1101'))      # False 
print(turing_machine('1101101'))   # False 
print(turing_machine('110110111')) # False 

 

Output: 

True 

True 

True 

False 

False 

False 

False 

 
