class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        p1 = 0
        maxLen = 0
        for p2, i in enumerate(s):
            while i in seen:
                seen.remove(s[p1])
                p1 += 1
            seen.add(i)
            maxLen = max(maxLen, p2 - p1 + 1)
        return maxLen

        