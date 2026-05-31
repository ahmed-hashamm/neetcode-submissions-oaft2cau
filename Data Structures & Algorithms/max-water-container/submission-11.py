class Solution:
    def maxArea(self, heights: List[int]) -> int:
        p1, p2 = 0, len(heights) - 1
        maxArea = 0
        while p1 < p2:
            height = min(heights[p1], heights[p2])
            maxArea = max(maxArea, height * (p2 - p1))
            if heights[p1] < heights[p2]:
                p1 += 1
            else:
                p2 -= 1
        return maxArea