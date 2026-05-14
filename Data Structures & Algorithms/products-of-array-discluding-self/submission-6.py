class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        if nums.count(0) > 1 : return [0] * len(nums)
        res = []
        product = math.prod(nums)
        prod_without_0 = 1
        for n in nums:
            if n == 0:continue
            else:
                prod_without_0 *= n
        
        for n in nums:
            if n == 0:
                res.append(prod_without_0)
            else:
                res.append(int(product/n))
        return res