class Solution:
    def maxArea(self, heights: List[int]) -> int:
        hashmap = []
        for i in range(len(heights)):
            for j in range(len(heights)):
                max_area = min(heights[i],heights[j]) * (j - i)
                hashmap.append(max_area)
        return max(hashmap)
            
        