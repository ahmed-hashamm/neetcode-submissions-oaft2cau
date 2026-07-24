class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = ""
        for l in s:
            if l.isalnum():
                st += l.lower()
        l = 0
        r = len(st) - 1
        while l < r:
            if st[l] != st[r]: return False
            l += 1
            r -= 1
        return True