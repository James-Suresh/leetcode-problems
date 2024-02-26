class Solution(object):
    def finalValueAfterOperations(self, operations):
        """
        :type operations: List[str]
        :rtype: int
        """
        x=0
        for n in operations:
            if '-' in n:
                x=x-1
            elif '+' in n:
                x=x+1
        return x