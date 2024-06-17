var MinStack = function() {
  this.mainStack = [];
  this.minStack = [];
};

/** 
* @param {number} val
* @return {void}
*/
MinStack.prototype.push = function(val) {
  this.mainStack.push(val);
  this.minStack.push(this.minStack.length !== 0? Math.min(this.minStack[this.minStack.length - 1], val) : val);
};

/**
* @return {void}
*/
MinStack.prototype.pop = function() {
  this.mainStack.pop();
  this.minStack.pop();
};

/**
* @return {number}
*/
MinStack.prototype.top = function() {
  return this.mainStack[this.mainStack.length-1];
};

/**
* @return {number}
*/
MinStack.prototype.getMin = function() {
  return this.minStack[this.minStack.length-1];
};

/** 
* Your MinStack object will be instantiated and called as such:
* var obj = new MinStack()
* obj.push(val)
* obj.pop()
* var param_3 = obj.top()
* var param_4 = obj.getMin()
*/

var obj = new MinStack();
obj.push(3);
obj.push(5);
obj.push(6);
obj.push(2);
obj.push(4);
obj.push(1);
console.log(...obj.minStack);