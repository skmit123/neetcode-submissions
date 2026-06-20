class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        aim = nums1 + nums2
        aim.sort()
        if len(aim) % 2 == 0:
            return (aim[len(aim) // 2 - 1] + aim[len(aim) // 2]) / 2.0
        else:
            return aim[len(aim) // 2]
        