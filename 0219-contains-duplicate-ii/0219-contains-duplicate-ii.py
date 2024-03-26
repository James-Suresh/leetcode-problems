class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        hm={}
        
        for i, n in enumerate(nums):
            if n in hm:
                if abs(i - hm[n])<= k:
                    return True
            hm[n] = i
        return False
                