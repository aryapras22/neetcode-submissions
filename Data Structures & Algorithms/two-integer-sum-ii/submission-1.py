class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        seen = {}
        for i, n in enumerate(numbers):
            k = target - n
            if n in seen:
                return [seen[n]+1, i+1]
            seen[k] = i
            # print(f"k: {k}, i: {i}, {seen}")
        return []