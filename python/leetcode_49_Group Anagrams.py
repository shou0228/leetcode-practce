class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for string in strs:
            sorted_str = ''.join(sorted(string))
            res[sorted_str].append(string)
        return res.values()
