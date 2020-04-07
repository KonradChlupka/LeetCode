class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ordered_to_list = collections.defaultdict(list)
        for word in strs:
            key = tuple(sorted(word))
            ordered_to_list[key].append(word)
        return ordered_to_list.values()
