class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        seen, used = set(), set()
        for i in range(len(nums)):
            for j in range(i + 1, len(nums)):
                k = nums[i] + nums[j]
                thirdNum = abs(k) if k < 0 else - k
                hash = str(sorted([nums[i], nums[j], thirdNum]))
                if thirdNum in seen and hash not in used:
                    res.append([nums[i], nums[j], thirdNum])
                    used.add(hash)
            seen.add(nums[i])
        return res