"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        old_to_copy = { None: None }
        currNode = head
        while currNode:
            copy = Node(currNode.val)
            old_to_copy[currNode] = copy
            currNode = currNode.next
        
        currNode = head
        while currNode:
            copy = old_to_copy[currNode]
            copy.next = old_to_copy[currNode.next]
            copy.random = old_to_copy[currNode.random]
            currNode = currNode.next
        
        return old_to_copy[head]