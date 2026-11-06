# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:

    def getNumberFromList(self, l: ListNode):
        temp = l

        num = 0
        i = 0
        while temp:
            num = num + (temp.val * 10**i)
            i = i + 1
            temp = temp.next
        return num

    def addTwoNumbers(
        self, l1: Optional[ListNode], l2: Optional[ListNode]
    ) -> Optional[ListNode]:
        num1 = self.getNumberFromList(l1)
        num2 = self.getNumberFromList(l2)
        summed = num1 + num2

        digits = [int(digit) for digit in str(summed)]

        temp = ListNode(val=digits[0])
        for digit in digits[1:]:
            temp = ListNode(val=digit, next=temp)

        return temp
