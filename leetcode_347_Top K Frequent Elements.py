#邏輯迴圈解法
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:      
        count = {}
        freq = [[] for i in range(len(nums) + 1)]

        for n in nums:
            count[n] = 1 + count.get(n, 0) 
				#it will return zero if it doesn't exist

        for n, c in count.items():
            freq[c].append(n) 
				#value n occurs c number of times

        res = []
        for i in range(len(freq) - 1, 0, -1): #此為降冪排列（第三個為負，由大到小排）
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
#Counter function解法
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counter = Counter(nums).most_common()
        res = [counter[i][0] for i in range(k)]
        return res
