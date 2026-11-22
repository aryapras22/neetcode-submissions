class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # First things i need to calculate each word characteristic
        # after that i could group them into same characteristic
        group_list = []
        word_map = {}
        for word in strs:
            sorted_word = "".join(sorted(word))
            if sorted_word not in word_map:
                word_map[sorted_word] = []
            word_map[sorted_word].append(word)

        for key, value in word_map.items():
            group_list.append(value)
        return group_list
            