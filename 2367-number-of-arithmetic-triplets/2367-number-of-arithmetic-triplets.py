class Solution(object):
    def arithmeticTriplets(self, nums, diff):
        """
        :type nums: List[int]
        :type diff: int
        :rtype: int
        """
        nums_set = set(nums)
        counter=0
        a=0
        b=0
        for i,n in enumerate(nums_set):
            a = n-diff
            b = n+diff

            if a in nums_set and b in nums_set:
                counter+=1
        return counter
        

            