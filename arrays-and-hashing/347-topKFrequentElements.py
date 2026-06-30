class Solution:

    """
    Sorting approach.
    Time complexity: O(n log n), where n is the length of nums
    Space complexity: O(n)
    """
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        numDict = {} # maps num to the num's frequency
        for num in nums:
            numDict[num] = 1 + numDict.get(num, 0)
        
        pairs = [] # list of [frequency, integer] pairs
        for i, freq in numDict.items():
            pairs.append([freq, i])

        pairs.sort() # sort most frequent -> least in O(n log n)

        res = []
        for i in range(k):
            res.append(pairs.pop()[1]) # pop the k most frequent elements
        
        return res