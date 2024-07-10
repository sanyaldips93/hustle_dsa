class Solution:
  def countNodesinLoop(head):
    #Your code here
    slow, fast = head, head
    count = 0
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
        if slow == fast:
            slow = slow.next
            count += 1
            while slow != fast:
                slow = slow.next
                count += 1
            return count
    return count
  
print(Solution().countNodesinLoop()) # pass your linked list head