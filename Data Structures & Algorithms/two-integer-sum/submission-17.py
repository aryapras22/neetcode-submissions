class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
    # the obvious solution will be iterate each item on array with another item, which gonna result in O(n^2)
        for index, num in enumerate(nums):
            for key in range(index + 1, len(nums)):
                if nums[key] + num == target:
                    return [index, key]
        return []