def verify_parentheses(input_str):
    stack = []
    
    for char in input_str:
        if char == '(':
            stack.append(char)
        elif char == ')':
            if not stack or stack.pop() != '(':
                return 'incorrect'
    
    if stack:
        return 'incorrect'
    else:
        return 'correct'

try:
    input_int = int(input())
except ValueError:
    exit()

for i in range(input_int):
    input_str = input()
    print(verify_parentheses(input_str))
