# Valid Parentheses - check if brackets are balanced
def is_valid(s):
    stack = []
    mapping = {")": "(", "}": "{", "]": "["}
    for ch in s:
        if ch in mapping:
            top = stack.pop() if stack else "#"
            if mapping[ch] != top:
                return False
        else:
            stack.append(ch)
    return not stack

print(is_valid("()[]{}"))   # True
print(is_valid("(]"))       # False
print(is_valid("{[]}"))     # True
