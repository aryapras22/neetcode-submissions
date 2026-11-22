class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # i, j = 0, 0
        # for i in range(len(nums)):
        #      for j in range(len(nums)):
        #         if(i != j):
        #             sum = nums[i] + nums[j]
        #             if(sum == target):
        #                 return [i, j]
        # return []

        num_map = {}

        for i, num in enumerate(nums):
            complement = target - num

            if complement in num_map:
                return [num_map[complement], i]
            
            num_map[num] = i

        return []
        