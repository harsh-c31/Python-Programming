def isoperat(x):
    if x=='+':
        return True
    if x=='-':
        return True
    if x=='*':
        return True
    if x=='/':
        return True
    return False
def postfixtoprefix(post_exp):
    s=[]
    l=len(post_exp)
    for i in range(l):
        if (isoperat(post_exp[i])):
            op1=s[-1]
            s.pop()
            op2=s[-1]
            s.pop()
            tem=post_exp[i]+op2+op1
            s.append(tem)
        else:
            s.append(post_exp[i])
    ans=""
    for i in s:
        ans=ans+i
    return ans
if __name__ == "__main__":

    post_exp = "AB+CD-"
    
    # Function calld
    print("Prefix : ", postfixtoprefix(post_exp))