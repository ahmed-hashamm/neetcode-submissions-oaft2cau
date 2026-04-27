class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            hash = tuple(sorted(s))
            groups[hash].append(s)
        return list(groups.values())