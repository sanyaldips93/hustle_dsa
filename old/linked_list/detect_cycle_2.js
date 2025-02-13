/**
 * Definition for singly-linked list.
 * function ListNode(val) {
 *     this.val = val;
 *     this.next = null;
 * }
 */

// return the node where the cycle begins.

/**
 * @param {ListNode} head
 * @return {ListNode}
 */
var detectCycle = function(head) {
  let slow = head;
let fast = head;
while(fast && fast.next) {
    slow = slow.next;
    fast = fast.next.next;
    if(slow === fast) {
        let ptr = head;
        while(ptr !== slow) {
            ptr = ptr.next;
            slow = slow.next;
        }
        return ptr;
    }
}
return null;
};