def lengthOfLongestSubstring(s: str) -> int:
    chMap: dict[char, int] = {}
    i = 0
    maxLen = 0

    for j, ch in enumerate(s):
      if ch in chMap and chMap[ch] >= i:
        i = chMap[ch] + 1
      chMap[ch] = j
      maxLen = max(maxLen, j - i + 1)

    return maxLen    
         
print(lengthOfLongestSubstring("abcabcbb"))
print(lengthOfLongestSubstring("bbbbb"))
print(lengthOfLongestSubstring("pwwkew"))
print(lengthOfLongestSubstring(""))
print(lengthOfLongestSubstring("a"))
print(lengthOfLongestSubstring("this is a string"))
print(lengthOfLongestSubstring("abracadabra"))
