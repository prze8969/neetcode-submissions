class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left=0
        best = 0
        for right in range(len(s)):
            while s[right] in s[left:right]:
                left+=1
            best = max(right-left+1, best)
        return best

        