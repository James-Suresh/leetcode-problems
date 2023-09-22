class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """
        
        key1 = [0]*26
        key2 = [0]*26
        for char in s:
            key1[ord(char) - ord('a')] += 1
        for char in t:
            key2[ord(char) - ord('a')] += 1
        if key1 == key2:
            return True
        else:
            return False
        
        