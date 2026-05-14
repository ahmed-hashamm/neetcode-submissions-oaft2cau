class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += str(len(st)) + "#" + st
        return s 

    def decode(self, s: str) -> List[str]:
        res = []
        p1 = 0
        while p1 < len(s):
            p2 = p1
            while s[p2] != "#":
                p2 += 1
            len_st = int(s[p1:p2])
            res.append(s[p2 + 1: p2 + 1 + len_st])
            p1 = p2 + 1 + len_st
        return res


