#Reverse linked list using recursion

"""
https://www.youtube.com/watch?v=ugQ2DVJJroc
"""
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return head
        temp=head.next
        newHead=self.reverseList(temp)
        temp.next=head
        head.next=None
        return newHead