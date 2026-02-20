def strcomp(s):
    compressed_result=[]
    count=1
    for i in range(1,len(s)):
        if (s[i]==s[i-1]):
            count+=1
        else:
            compressed_result.append(s[i-1]+str(count))
            count=1
    compressed_result.append(s[-1]+str(count))
    str_compressed=''.join(compressed_result)
    if len(str_compressed)<len(s):
        return str_compressed
    else:
        return s
print(strcomp('aaaabbbbbccccccc'))    