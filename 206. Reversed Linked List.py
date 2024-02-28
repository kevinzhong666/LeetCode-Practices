class Solution(object):
    def reverseList(self, head):
      current = head
      prev = None
      while current != None :
          current.next = self
          current.next = prev
          prev = current
          current = next