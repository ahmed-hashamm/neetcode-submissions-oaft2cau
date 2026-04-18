class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = collections.defaultdict(list)
        for s in strs:
            key = str(sorted(list(s)))
            groups[key].append(s)
        return list(groups.values())