def lengthOfLongestSubstring(s: str) -> int:
    if len(s) == 0:
        return 0

    chMap: dict[str, int] = {}
    i: int = 0
    j: int = 0
    maxLen: int = 1

    chMap[s[0]] = 0
    j += 1 
    
    while j < len(s):
        if s[j] in chMap:
            k = chMap[s[j]] + 1
            while i < k:
                del chMap[s[i]]
                i += 1
        else:
            if (j - i) + 1 > maxLen:
                 maxLen = (j - i) + 1
            chMap[s[j]] = j
            j += 1
    
    return maxLen
         
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring("a"))
print(lengthOfLongestSubstring("this is a string"))
print(lengthOfLongestSubstring("abracadabra"))
