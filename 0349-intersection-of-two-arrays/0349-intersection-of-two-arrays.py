class Solution(object):
    def intersection(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """
        set1=set()
        
        if nums1>=nums2:
            for n in nums2: 
                if n in nums1:
                    set1.add(n)
        else:
            for n in nums1: 
                if n in nums2:
                    set1.add(n)
                    
        return set1