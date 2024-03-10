from typing import Optional

"""
Leetcode Q2 - Add Two Numbers
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order, and each of their nodes contains a single digit. Add the two numbers and return the sum as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

 
Example 1:


Input: l1 = [2,4,3], l2 = [5,6,4]
Output: [7,0,8]
Explanation: 342 + 465 = 807.
Example 2:

Input: l1 = [0], l2 = [0]
Output: [0]
Example 3:

Input: l1 = [9,9,9,9,9,9,9], l2 = [9,9,9,9]
Output: [8,9,9,9,0,0,0,1]
 

Constraints:

The number of nodes in each linked list is in the range [1, 100].
0 <= Node.val <= 9
It is guaranteed that the list represents a number that does not have leading zeros.
"""

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        stack = []

        current = l1
        while current:
            stack.append(current.val)
            current = current.next

        num1 = ""
        while stack:
            num1 += str(stack.pop())

        current = l2
        while current:
            stack.append(current.val)
            current = current.next

        num2 = ""
        while stack:
            num2 += str(stack.pop())

        total = str(int(num1) + int(num2))
        for digit in total:
            stack.append(digit)

        head = ListNode(int(stack.pop()), None)
        current = head
        while stack:
            current.next = ListNode(int(stack.pop()), None)
            current = current.next
        return head
