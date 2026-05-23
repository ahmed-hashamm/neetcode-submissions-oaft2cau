class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums)
        countVals = collections.defaultdict(list)
        for val, cnt in counter.items():
            countVals[cnt].append(val)
        
        cnts = [-cnt for cnt in countVals.keys()]
        heapq.heapify(cnts)

        res = []
        for i in range(len(cnts)):
            cnt2 = - heapq.heappop(cnts)
            for n in countVals[cnt2]:
                if len(res) == k: return res
                res.append(n)
        return res


        