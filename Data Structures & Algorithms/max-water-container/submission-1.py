class Solution:
    def maxArea(self, heights: List[int]) -> int:
        res = []
        left = 0
        right = len(heights) - 1
        while left < right:
            max_area = min(heights[left],heights[right]) * (right - left)
            res.append(max_area)
            if heights[left] <= heights[right]:
                left += 1
            else:
                right -= 1
            
        return max(res)

        