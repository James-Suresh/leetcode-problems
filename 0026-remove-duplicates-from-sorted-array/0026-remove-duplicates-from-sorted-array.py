class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        k=0
        expectedNums = []
        for index, num in enumerate(nums):
            if num in expectedNums:
                nums[index]='_'
            else:
                expectedNums.append(num)
                k = k+1
        nums.sort()
        print (nums)
        return k
            
                