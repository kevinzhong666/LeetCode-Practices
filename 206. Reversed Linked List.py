class Solution(object):
    def reverseList(self, head):
        current = head
        prev = None
        while current is not None:
            next_temp = current.next  # Temporarily store the next node
            current.next = prev       # Reverse the current node's pointer
            prev = current            # Move prev to current
            current = next_temp       # Move to the next node in the original list
        return prev  # prev is the new head of the reversed list
