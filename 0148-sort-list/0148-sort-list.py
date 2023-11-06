# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        nlist=[]
        curr = head 
        if head == None:
            return head
        while curr!=None:
            nlist.append(curr.val)
            curr=curr.next
        nlist.sort()
        
        curr = head
        
        i=0
        while curr!=None:
            curr.val=nlist.pop(0) 
            if i==0:
                newhead=curr
            curr=curr.next
            i+=1
            
        return newhead
            
                