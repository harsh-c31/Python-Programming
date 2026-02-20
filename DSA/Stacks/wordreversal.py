def wordrev(sen):
    result = ""
    stack = []
    
    for char in sen:
    #if not space
        if char != " ":
            stack.append(char)
        else:
            #when space comes
            while stack:
                result += stack.pop()
                #after one word reversal completes
            result += " "
    while stack:
        #poping result
        result += stack.pop()
    
    return result


print(wordrev("hello world"))
