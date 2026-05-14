class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        contains = set(nums)
        maxLen = 0
        for n in nums:
            if n - 1 in nums:continue
            curr, currLen = n, 0
            while curr in contains:
                curr += 1
                currLen += 1
            maxLen = max(currLen, maxLen)
        return maxLen