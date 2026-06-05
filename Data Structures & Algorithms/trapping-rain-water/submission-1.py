class Solution:
    def trap(self, heights: List[int]) -> int:
        res = []
        left = 0
        right = len(heights) - 1
        maxLeft, maxRight = heights[left], heights[right]
        while left < right:
            if maxLeft < maxRight:
                left += 1
                maxLeft = max(maxLeft,heights[left])
                res.append(maxLeft - heights[left])
            else:
                right -= 1
                maxRight = max(maxRight,heights[right])
                res.append(maxRight - heights[right])

        return sum(res)
 