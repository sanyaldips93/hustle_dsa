function Node(key, val, next, prev) {
  this.key = (key===undefined) ? 0 : key;
  this.val = (val===undefined ? 0 : val);
  this.next = (next===undefined ? null : next);
  this.prev = (prev===undefined ? null : prev);
}

var LRUCache = function(capacity) {
  this.capacity = capacity;
  this.size = 0;
  this.cache = {};
  this.left = new Node(0,0);
  this.right = new Node(0,0);
  this.left.next = this.right;
  this.right.prev = this.left;
};

LRUCache.prototype.get = function(key) {
  if(key in this.cache) {
    this.remove(this.cache[key]);
    this.insert(this.cache[key]);
    return this.cache[key].val;
  }
  return -1;
};

/** 
* @param {number} key 
* @param {number} value
* @return {void}
*/
LRUCache.prototype.put = function(key, value) {
  if(key in this.cache) {
    this.remove(this.cache[key]);
  }
  this.cache[key] = new Node(key, value);
  this.insert(this.cache[key]);

  if(this.capacity < this.size) {
    let lru = this.left.next;
    this.remove(lru);
    delete this.cache[lru.key];
  }
};

LRUCache.prototype.remove = function(node) {
  if(!(this.size === 0)) {
    let nextNode = node.next;
    let prevNode = node.prev;
    prevNode.next = nextNode;
    nextNode.prev = prevNode;
    this.size--;
  }
}

LRUCache.prototype.insert = function(node) {
  let prevNode = this.right.prev;
  prevNode.next = node;
  node.prev = prevNode;
  node.next = this.right;
  this.right.prev = node;
  this.size++;
}


var obj = new LRUCache(2);
console.log(obj.get(2));
obj.put(1,1);
obj.put(2,2);
console.log(obj.get(1));
obj.put(3,3);
console.log(obj.get(2));
obj.put(4,4);
console.log(obj.get(3));