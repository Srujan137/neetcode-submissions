class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqMap = {}
        op = set()
        mostfreq = 0
        for n in nums:
            freqMap[n] = 1 + freqMap.get(n,0)
        
        freq = [[] for i in range(len(nums) + 1)]

        for n,c in freqMap.items():
            freq[c].append(n)

        res = []

        for i in range(len(freq)-1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res

            

            

        
        