# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        numberInString = ''
        length = 0
        ans = 0
        while head != None:
            numberInString += str(head.val)
            length += 1
            head = head.next

        for i in range(length):
            ans = ans + int(numberInString[i]) * 2**(length -1 -i)
        return ans