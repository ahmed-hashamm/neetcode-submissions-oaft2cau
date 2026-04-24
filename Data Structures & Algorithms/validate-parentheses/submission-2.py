class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        lookup = {
            "}" : "{",
            ")" : "(",
            "]" : "["
        }
        for bracket in s:
            if bracket in lookup.values():
                stack.append(bracket)
            elif not stack or stack[-1] != lookup[bracket]:
                return False
            else:
                stack.pop()
        return not stack
        