class Solution:

    """
    Standard solution using a HashMap to track letter counts.
    Time complexity: O(n) - both loops over s and t are O(n)
    Space complexity: O(k), where k is the number of distinct chars in s
    """
    def isAnagram(self, s: str, t: str) -> bool:

        # if the lengths are different, they're guaranteed to not be anagrams 
        if len(s) != len(t): 
            return False

        letter_counts = {}

        for letter in s:
            letter_counts[letter] = letter_counts.get(letter, 0) + 1
        
        for letter in t:
            letter_counts[letter] = letter_counts.get(letter, 0) - 1 

            if letter_counts[letter] < 0: # negative -> t contains a char more times than s or one that is not in s
                return False

        return True
    
    """
    Non-HashMap solution using sorted(), since sorted anagrams should be the exact same string.
    Time complexity: O(n log n) - sorted() is O(n log n)
    Space complexity: O(1), conceptually (sorted() makes O(n), but for the sake of interviews O(1))
    """
    def isAnagramInPlace(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)