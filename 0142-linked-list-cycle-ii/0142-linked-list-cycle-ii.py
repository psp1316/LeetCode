# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution(object):
    def detectCycle(self, head):
        
        slow = head
        fast = head
        has_cycle = False
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            
            if slow == fast:
                has_cycle = True
                break
        
        if not has_cycle:
            return None
        
        # Reset slow pointer to head, keep fast pointer where they met
        slow = head
        while slow != fast:
            slow = slow.next
            fast = fast.next
        
        return slow