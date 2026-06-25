class Solution:
    
    """
    Standard solution for O(n) time.
    Time complexity: O(n) - iterate through list (O(n)), each set lookup is O(1)
    Space complexity: O(n) - worst case stores all n elements
    """
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()

        for num in nums: 
            if num in seen:
                return True
            seen.add(num)

        return False
    

    """
    One-line solution.
    Time complexity: O(n) - set(nums) is O(n), len() and comparison are O(1)
    Space complexity: O(n) - worst case stores all n elements
    """
    def containsDuplicateOneLine(self, nums: List[int]) -> bool:
        return len(nums) > len(set(nums))
    
    """
    In-place solution.
    Time complexity: O(n log n) - sorted() is avg O(n log n)
    Space complexity: O(1) - technically, Python's sorted() does create a separate list, 
                                but conceptually no separate data structure is created
    """
    def containsDuplicateInPlace(self, nums: List[int]) -> bool:
        nums = sorted(nums)

        for i in range(1, len(nums)):
            if nums[i] == nums[i-1]:
                return True
            
        return False