class Solution(object):
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        hm = {}
        m=len(nums)/2
        for n in nums:
            hm[n] = hm.get(n, 0) + 1
            if hm[n]>m:
                return n
            
        