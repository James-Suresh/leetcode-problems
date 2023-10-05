class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        nset = set(nums)
        longest = 0 
        for n in nset:
            if ((n-1) not in nset): 
                count=1
                while ((n + count) in nset):
                    count+=1
                longest = max(longest, count)

        return longest