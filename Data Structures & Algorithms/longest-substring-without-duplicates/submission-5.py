class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        contains = set()
        maxLen = 0
        p1 = 0
        for p2, l in enumerate(s):
            while l in contains:
                contains.remove(s[p1])
                p1 += 1
            contains.add(l)
            maxLen = max(maxLen, p2 - p1 + 1)
        return maxLen
