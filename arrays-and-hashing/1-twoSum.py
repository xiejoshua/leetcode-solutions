class Solution:

    """
    Time complexity: O(n) - iterates through n elements of enumerate()
    Space complexity: O(n) - worst case numsDict stores all elements of nums
    """
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        numsDict = {}

        for i, num in enumerate(nums): # enumerate() allows you to iterate through a dict using both index and value
            complement = target - num

            if numsDict.get(complement, None) != None:
                return [i, numsDict[complement]]
            
            numsDict[num] = i