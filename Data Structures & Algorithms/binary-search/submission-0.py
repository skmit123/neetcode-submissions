class Solution:
    def search(self, nums: List[int], target: int) -> int:
        temp = []

        for i in range(len(nums)):
            temp.append(nums[i])

            if target in temp:
                return temp.index(target)

        return -1