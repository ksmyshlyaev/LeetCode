# # https://leetcode.com/problems/middle-of-the-linked-list/description/
# NOT SOLVED!
# from typing import Optional
# from precompiled.listnode.ListNode
#
#
# # Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
#
#
# class Solution:
#     def middleNode(self, head: Optional[ListNode]) -> Optional[ListNode]:
#         # middle = int(round((len(head) / 2)))
#         # return head[middle:len(head)]
#         list = [head.val for head.next in head]
#         print(list)
#
# if __name__ == '__main__':
#     print(Solution().middleNode([1, 2, 3, 4, 5, 6]))
#     print(Solution().middleNode([1, 2, 3, 4, 5]))
