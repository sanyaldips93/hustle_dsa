/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} l1
 * @param {ListNode} l2
 * @return {ListNode}
 */
var addTwoNumbers = function(l1, l2) {
  const res = new ListNode(0);
  let cur = res;
  let carry = 0;
  while(carry || l1 || l2) {
      const v1 = l1 ? l1.val : 0;
      const v2 = l2 ? l2.val : 0;
      let val = carry + v1 + v2;
      carry = Math.trunc(val / 10);
      val = val % 10;
      cur.next = new ListNode(val);
      cur = cur.next;
      l1 = l1 ? l1.next : null;
      l2 = l2 ? l2.next : null;
  }
  return res.next;
};