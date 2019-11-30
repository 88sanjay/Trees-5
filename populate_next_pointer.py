"""
# Definition for a Node.
class Node:
    def __init__(self, val: int = 0, left: 'Node' = None, right: 'Node' = None, next: 'Node' = None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""
class Solution:
    def connect(self, root: 'Node') -> 'Node':
        level = root    
        while level != None : # use level pointer 
            prev = None
            curr = level
            prev_right = None
            while curr and (curr.left) : # keep iterating in through the level and set the left connections for the children
                if curr.left :
                    curr.left.next = curr.right
                    if prev_right != None :
                        prev_right.next = curr.left
                    prev_right = curr.right
                curr = curr.next
            level = level.left
        return root
            
