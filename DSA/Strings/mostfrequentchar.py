def freqchar(s):
    freq = {}
    for ch in s:
        if ch in freq:
            freq[ch] += 1
        else:
            freq[ch] = 1
    max_count = 0
    for count in freq.values():
        if count > max_count:
            max_count = count
    return max_count
print(freqchar("haaaarssh"))
