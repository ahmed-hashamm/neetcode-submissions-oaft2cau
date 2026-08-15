class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = collections.defaultdict(list)
        for s in strs:
            hash = tuple(sorted(s))
            res[hash].append(s)
        return list(res.values())