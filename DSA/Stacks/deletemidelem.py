def delete_middle(stack):
    size = len(stack)
    def solve(stack, current):
        if current == size // 2:
            stack.pop()
            return
        temp = stack.pop()
        solve(stack, current + 1)
        stack.append(temp)
    
    solve(stack, 0)
    return stack

s = [1, 2, 3, 4, 5]
print("Original Stack:", s)
delete_middle(s)
print("After Deleting Middle:", s)
