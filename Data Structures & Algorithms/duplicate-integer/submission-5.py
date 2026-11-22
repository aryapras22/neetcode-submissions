class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        
        my_map = {}

        for i, num in enumerate(nums):
            if num in my_map:
                return True
            my_map[num] = i

        return False