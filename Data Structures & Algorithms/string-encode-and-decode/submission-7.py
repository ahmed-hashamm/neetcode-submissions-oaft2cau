class Solution:

    def encode(self, strs: List[str]) -> str:
        s = ""
        for st in strs:
            s += str(len(st)) + "&" + st
        return s


    def decode(self, s: str) -> List[str]:
        p1 = 0
        res = []
        while p1 < len(s):
            p2 = p1
            while s[p2] != "&":
                p2 += 1
            lenSt = int(s[p1:p2])
            res.append(s[p2 + 1: p2 + 1 + lenSt])
            p1 = p2 + 1 + lenSt
        return res

            

