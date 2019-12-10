# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        re = ListNode(0)
        carry = 0
        l3 = re
        while(l1 or l2):
            x = l1.val if l1 else 0
            y = l2.val if l2 else 0
            s = x + y + carry
            carry = s // 10
            l3.next = ListNode(s%10)
            l3 = l3.next
            if(l1!=None):
                l1 = l1.next
            if(l2!=None):
                l2 = l2.next
        if carry > 0 :
            l3.next = ListNode(1)
        return re.next

# 链表法 
# 套路： (1) 先定义一个空链表re作为返回值
#        (2) re 链表 next 指向最后的结果
#        (3) 链表循环 --> while
#        (4) 循环里每一次都需要定义l3.next = ListNode(s%10) l3 = l3.next
#        (5) 边界判定 最后carry>0时， 最后增加一位
