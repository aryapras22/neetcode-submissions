class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        # i need to count frequency of numbers and store it somewhere
        # i was think to store it to hashmap, and then sort and get top k from that hashmap
        num_hash = {}
        for index, num in enumerate(nums):
            num_hash[num] = num_hash.get(num, 0) + 1

        # print(num_hash)
        sorted_hash = sorted(num_hash.items(), key=lambda x: x[1], reverse=True)
        result = []
        for item in sorted_hash[:k]:
            result.append(item[0])

        return result