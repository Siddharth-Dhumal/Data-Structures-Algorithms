# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        nodes = []

        for li in lists:
            while li:
                nodes.append(li.val)
                li = li.next
        
        nodes.sort()

        dummy = ListNode(0)
        cur = dummy
        for node in nodes:
            cur.next = ListNode(node)
            cur = cur.next
        
        return dummy.next