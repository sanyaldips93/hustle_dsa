# https://www.geeksforgeeks.org/problems/flattening-a-linked-list

class Node:
    def __init__(self, d):
        self.data=d
        self.next=None
        self.bottom=None

def flatten(head):
    #Your code here
    if not head or not head.next:
        return head
    
    mergedhead = flatten(head.next)
    head = merge(head, mergedhead)
    return head
    
def merge(list1, list2):
    dummy = Node(-1)
    cur = dummy
    while list1 and list2:
        if list1.data < list2.data:
            cur.bottom = list1
            cur = list1
            list1 = list1.bottom
        else:
            cur.bottom = list2
            cur = list2
            list2 = list2.bottom
        cur.next = None
    if list1:
        cur.bottom = list1
    if list2:
        cur.bottom = list2
    if dummy.bottom:
        dummy.bottom.next = None
    return dummy.bottom