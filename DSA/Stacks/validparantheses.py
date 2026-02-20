def validp(s):
    stackk = []
    
    for c in s:
        if c == '(' or c == '{' or c == "[":
            stackk.append(c)
            
        elif c == ")" or c == "}" or c == "]":
            if not stackk:
                return False
                
            top = stackk[-1]
            
            if ((c == ')' and top != '(') or
                (c == '}' and top != '{') or 
                (c == ']' and top != '[')):
                return False
                
            stackk.pop()
                
    return not stackk


if __name__ == '__main__':
    s = "[()()]{}"
    print("true" if validp(s) else "false")
