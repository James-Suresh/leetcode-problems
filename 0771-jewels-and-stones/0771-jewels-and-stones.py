class Solution(object):
    def numJewelsInStones(self, jewels, stones):
        """
        :type jewels: str
        :type stones: str
        :rtype: int
        """
        j_list = list(jewels)
        
        count = 0
        for c in stones:
            if c in j_list:
                count +=1
        
        return count
    