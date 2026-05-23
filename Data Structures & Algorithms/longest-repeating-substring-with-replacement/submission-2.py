class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        counter = defaultdict(int)
        p1 = maxFre = maxLen = 0
        for p2, l in enumerate(s):
            counter[l] += 1
            maxFre = max(maxFre, counter[l])
            while (p2 - p1 + 1) - maxFre - k > 0:
                counter[s[p1]] -= 1
                p1 += 1
            maxLen = max(maxLen, (p2 - p1 + 1))
        return maxLen
                