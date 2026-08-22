class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        window_chars = {}
        length = 0

        for right in range(len(s)):
            char = s[right]

            if char in window_chars and window_chars[char] >= left:
                left = window_chars[char] + 1

            window_chars[char] = right

            l = right-left+1
            if l > length:
                length = l
        return length
