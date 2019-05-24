# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        l1ptr = l1
        l2ptr = l2
        curr = head = ListNode(0)
        num1 = 0
        num2 = 0
        carry = 0
        while (l1ptr != None or l2ptr != None):
            if l1ptr != None:
                num1 = l1ptr.val 
            else:
                num1 = 0
            if l2ptr != None:
                num2 = l2ptr.val 
            else:
                num2 = 0
            result = num1 + num2 + carry
            curr.next = ListNode(result % 10)
            carry = result // 10
            if l1ptr != None: l1ptr = l1ptr.next
            if l2ptr != None: l2ptr = l2ptr.next
            curr = curr.next
            
        if carry > 0:
            curr.next = ListNode(carry)
            
        return head.next
