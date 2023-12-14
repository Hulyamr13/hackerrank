def isBalanced(s):
    stack = []
    brackets = {'{': '}', '[': ']', '(': ')'}

    for bracket in s:
        if bracket in brackets:  # If it's an opening bracket, push onto stack
            stack.append(bracket)
        else:
            if not stack or brackets[stack.pop()] != bracket:  # If it's a closing bracket
                return "NO"

    return "YES" if not stack else "NO"


# Reading input from STDIN
if __name__ == '__main__':
    n = int(input())
    for _ in range(n):
        s = input()
        result = isBalanced(s)
        print(result)
