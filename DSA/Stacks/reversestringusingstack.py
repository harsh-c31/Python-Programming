def revstring(s):
    stack=[]
    for ch in s:
        stack.append(ch)
    rev_string=""
    while stack:
        rev_string+=stack.pop()
    return rev_string
if __name__=='__main__':
    s="GeeksforGeeks"
    print(revstring(s))