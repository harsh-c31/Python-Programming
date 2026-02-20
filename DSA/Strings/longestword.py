def longest(s):
    words=s.split()
    longest=""
    for word in words:
        if len(word)>len(longest):
            longest=word
    return longest
print(longest("hello my name is haararsh tyagaaaai"))