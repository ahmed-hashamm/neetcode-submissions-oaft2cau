class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        seen = set(nums)
        maxLen = 0
        for n in nums:
            if n - 1 in nums:continue
            curr, currLen = n, 0
            while curr in seen:
                curr += 1
                currLen += 1
            maxLen = max(maxLen, currLen)
        return maxLen
        