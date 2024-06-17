/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @return {void} Do not return anything, modify head in-place instead.
 */
var reorderList = function(head) {
  // find middle of the linkedlist
  let slow = head;
  let fast = head.next;
  while(fast && fast.next) {
      slow = slow.next;
      fast = fast.next.next;
  }

  let second = slow.next;
  let prev = null;
  slow.next = null;

  // reverse the second ll
  while(second) {
      let tmp = second.next;
      second.next = prev;
      prev = second;
      second = tmp;
  }

  // reorganizing;
  let h = head;
  let t = prev;
  while(t) {
      let tmp1 = h.next;
      let tmp2 = t.next;
      h.next = t;
      t.next = tmp1;
      h = tmp1;
      t = tmp2;
  }
};