# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        
        if not head:
            return head
        
        node=head
        stack=[node]
        
        while node.next!=None:
            node=node.next
            stack.append(node)
        
        if len(stack)==1:
            return stack[0]

        if k>len(stack):
            k = int(k)
            k = (k % len(stack))+len(stack) 
            

        while(k>0):
            newhead=stack.pop()
            newhead.next=stack[0]
            stack = [newhead] + stack
            stack[-1].next=None
            k-=1
            
        return stack[0]



        
            
