class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        longestStr = 0
        index = 0
        head = 0
        hash = {}
        while(index < len(s)):
            char = s[index]
            if char in hash and hash[char] >= head:
                if count > longestStr: longestStr = count
                char_index = hash[char]
                count = index - char_index
                head = char_index + 1
                hash[char] = index
            else:
                hash[char] = index
                count += 1
            index += 1
        return max(count, longestStr)
