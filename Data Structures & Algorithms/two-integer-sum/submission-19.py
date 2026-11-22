class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # the obvious solution will be iterate each item on array with another item, which gonna result in O(n^2)
        # for index, num in enumerate(nums):
        #     for key in range(index + 1, len(nums)):
        #         if nums[key] + num == target:
        #             return [index, key]
        # return []
    
    # so the efficient way should be cutting the for loop here,
    # another approach can be by leveraging the hash, which we can use the target as key to finding our desired indexes
        nums_hash = {}
        for index, num in enumerate(nums):
            if nums_hash.get(target - num) != None:
                return [nums_hash[target - num], index]
            nums_hash[num] = index
        
        return []
