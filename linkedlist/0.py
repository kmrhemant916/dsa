#Reverse linked list

"""
# Idea - you have to 3 pointer and slide that pointer on every iteration
https://www.youtube.com/watch?v=ugQ2DVJJroc
# Node Class

class node:
    def __init__(self, val):
        self.data = val
        self.next = None

"""

class Solution:
    def reverseList(self, head):
        prev=None
        curr=head
        temp=curr.next
        if head.next is None:
            return head
        while temp is not None:
            curr.next=prev
            prev=curr
            curr=temp
            temp=temp.next
        curr.next=prev
        return curr