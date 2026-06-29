class Solution:
    """
    Solution using a HashMap of "count lists".

    Time complexity - O(m * n), where m is the # of strings in strs and n is the avg. length of each string
    Space complexity - O(m * n), same as above
    """
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # maps a specific "count list" to a list of strings with that   same "count list". defaultdict prevents no key exists errors when appending later

        for s in strs:
            count = [0] * 26 # creates a list for counts of each letter, with index 0 representing the # of a's, 1 being the # of b's, etc

            for char in s:
                count[ord(char) - ord('a')] += 1
            
            res[tuple(count)].append(s) # Python dictionaries can't use lists as keys, so must convert to tuple; tuple() is O(n) in Python
        
        return list(res.values()) # list() is again O(n)