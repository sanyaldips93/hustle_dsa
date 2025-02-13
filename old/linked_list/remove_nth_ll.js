/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} n
 * @return {ListNode}
 */
var removeNthFromEnd = function(head, n) {
  const dummy = new ListNode(); // "0" 
  dummy.next = head; // "0" -> 1 -> 2 -> 3 -> 4 -> 5
  let left = dummy; // l - 0
  let right = head; // r - 1
  while(n>0 && right) {
      right = right.next;
      n--;
  }
  // right = 3
  while(right) {
      right = right.next;
      left = left.next;
  }
  // right = 5; left = 2;

  left.next = left.next.next;
  return dummy.next;
};