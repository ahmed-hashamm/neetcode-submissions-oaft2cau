class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        countVals = collections.defaultdict(list)
        counter = Counter(nums)
        for num, cnt  in counter.items():
            countVals[cnt].append(num)
        cnts = [- cnt for cnt in countVals.keys()]
        heapq.heapify(cnts)

        res = []
        for i in range(len(cnts)):
            pop = - heapq.heappop(cnts)
            for n in countVals[pop]:
                if len(res) == k: return res
                res.append(n)
        return res
