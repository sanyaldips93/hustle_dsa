/**
 * Definition for singly-linked list.
 * function ListNode(val, next) {
 *     this.val = (val===undefined ? 0 : val)
 *     this.next = (next===undefined ? null : next)
 * }
 */
/**
 * @param {ListNode} head
 * @param {number} k
 * @return {ListNode}
 */
var reverseKGroup = function(head, k) {
  let dummy = new ListNode(0, head);
  groupPrev = dummy;

  while(true) {
      let kth = getKth(groupPrev, k);
      if(!kth) {
          break;
      }
      let groupNext = kth.next;
      let prev = kth.next;
      let curr = groupPrev.next;
      while(curr !== groupNext) {
          let tmp = curr.next;
          curr.next = prev;
          prev = curr;
          curr = tmp;
      }
      let tmp = groupPrev.next;
      groupPrev.next = kth;
      groupPrev = tmp;
  }
  return dummy.next;
  

  function getKth(curr, k) {
      while(curr && k) {
          curr = curr.next;
          k -= 1;
      }
      return curr;
  }
};

function ListNode(val, next) {
  this.val = (val===undefined ? 0 : val)
  this.next = (next===undefined ? null : next)
}

const a = new ListNode(5);
const b = new ListNode(4,a);
const c = new ListNode(3,b);
const d = new ListNode(2,c);
const e = new ListNode(1,d);

console.log(reverseKGroup(e, 2));