import re

def tokenize(expression):
    """Convert expression string into tokens (numbers and operators)"""
    # Remove all spaces
    expression = expression.replace(' ', '')
    
    # Use regex to find numbers (including decimals) and operators
    token_pattern = r'(\d+\.?\d*|[-+*/()])'
    tokens = re.findall(token_pattern, expression)
    
    # Convert number tokens to floats, leave operators as strings
    result = []
    for token in tokens:
        if token in '+-*/()':
            result.append(token)
        else:
            result.append(float(token))
    
    return result

def has_precedence(op1, op2):
    """Check if op1 has higher or equal precedence than op2"""
    precedence = {'+': 1, '-': 1, '*': 2, '/': 2}
    return precedence.get(op1, 0) >= precedence.get(op2, 0)

def apply_operator(operators, values):
    """Apply the top operator to the top two values"""
    operator = operators.pop()
    right = values.pop()
    left = values.pop()
    
    if operator == '+':
        values.append(left + right)
    elif operator == '-':
        values.append(left - right)
    elif operator == '*':
        values.append(left * right)
    elif operator == '/':
        values.append(left / right)

def evaluate(tokens):
    """Evaluate expression using Dijkstra's Shunting Yard algorithm"""
    values = []     # Stack for values
    operators = []  # Stack for operators
    
    i = 0
    while i < len(tokens):
        token = tokens[i]
        
        # If it's a number, push to values stack
        if isinstance(token, float):
            values.append(token)
        
        # If it's an opening parenthesis, push to operators stack
        elif token == '(':
            operators.append(token)
        
        # If it's a closing parenthesis, solve entire parenthetical expression
        elif token == ')':
            while operators and operators[-1] != '(':
                apply_operator(operators, values)
            operators.pop()  # Remove the opening parenthesis
        
        # If it's an operator
        else:
            while (operators and operators[-1] != '(' and 
                   has_precedence(operators[-1], token)):
                apply_operator(operators, values)
            operators.append(token)
        
        i += 1
    
    # Apply remaining operators
    while operators:
        apply_operator(operators, values)
    
    return values[0] if values else 0

def main():
    print("Terminal Calculator")
    print("Enter expressions with numbers and operators (+, -, *, /)")
    print("Use parentheses for grouping. Type 'quit' to exit.")
    print()
    
    while True:
        try:
            expression = input("> ").strip()
            
            if expression.lower() == 'quit':
                break
            if not expression:
                continue
            
            tokens = tokenize(expression)
            result = evaluate(tokens)
            print(f"= {result}")
            
        except (ValueError, IndexError, ZeroDivisionError):
            print("Error: Invalid expression")
        except KeyboardInterrupt:
            print("\nGoodbye!")
            break

if __name__ == "__main__":
    main()