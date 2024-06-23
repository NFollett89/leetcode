# https://leetcode.com/problems/longest-substring-without-repeating-characters/
#
# Intuition
# - Brute force seems like a nested for loop, or I could use recursion
# - Using a map for the current substring's characters will help performance vs. a list of characters


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s) == 1:
            return 1
        longest = 0
        for start in range(len(s) - 1):
            longest = max(longest, self._findLengthUnique(s[start:]))
        return longest

    def _findLengthUnique(self, s: str) -> int:
        chars = {}
        for c in s:
            if not chars.get(c):
                chars[c] = True
            else:
                break
        return len(chars)
