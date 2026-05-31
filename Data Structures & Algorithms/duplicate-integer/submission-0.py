class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
    
        counter = []
        for i in nums:
            if i  in counter:
                return True
            counter.append(i)
        return False