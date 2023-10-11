class Solution(object):
    def twoSum(self, numbers, target):
        """
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        
        for i in range(len(numbers)):
            print numbers[i]
            
        p1 = 0
        p2 = len(numbers) - 1
        while True:
            if numbers[p1] + numbers[p2] > target:
                p2 -= 1
            if numbers[p1] + numbers[p2] < target:
                p1 += 1
            if numbers[p1] + numbers[p2] == target:
                return [p1+1,p2+1]

        

