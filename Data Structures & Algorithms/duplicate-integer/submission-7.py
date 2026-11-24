class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        nums_map={}
        for index, num in enumerate(nums):
            if num in nums_map:
                return True
            nums_map[num] = index
        
        return False