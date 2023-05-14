# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # length = 0
        # node = head
        # while node != None:
        #     length += 1
        #     node = node.next
        
        # half = length/2 
        # node = head
        # for i in range(int(half)):
        #     node = node.next
        # return node

        temp = head
        while temp and temp.next:
            head = head.next
            temp = temp.next.next
        return head