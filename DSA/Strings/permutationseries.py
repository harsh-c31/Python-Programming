def findpermutations(s):
    if len(s)==1:
        return s
    permutations=[]
    for i in range(len(s)):
        curr_char=s[i]
        remaining_char=s[:i]+s[i+1:]
        remaining_permutations=findpermutations(remaining_char)
        for p in remaining_permutations:
            permutations.append(curr_char+p)
    return permutations
print(findpermutations('abc'))