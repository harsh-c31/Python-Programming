def validp(s):
    stack = []
    pairs = {')': '(', '}': '{', ']': '['}
    
    for c in s:
        if c in pairs.values():      # opening bracket
            stack.append(c)
        elif c in pairs:             # closing bracket
            if not stack or stack[-1] != pairs[c]:
                return False
            stack.pop()
    
    return not stack
if __name__ == '__main__':
    s = "[()()]{}"
    print("true" if validp(s) else "false")
