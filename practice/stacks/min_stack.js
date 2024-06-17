class MinStack {
    constructor() {
        this.mainStack = [];
        this.minStack = [];
    }

    push(val) {
        this.mainStack.push(val);
        this.minStack.push(this.minStack.length !== 0 ? Math.min(val, this.minStack[this.minStack.length - 1]) : val); 
    }

    getTop() {
        return this.mainStack[this.mainStack.length - 1];
    }

    getMin() {
        return this.minStack[this.minStack.length - 1];
    }

    pop() {
        this.mainStack.pop();
        this.minStack.pop();
    }

    print() {
      console.log(this.mainStack);
      console.log(this.minStack);
    }
}

const obj = new MinStack();
obj.push(6);
obj.push(4);
obj.push(3);
obj.push(8);
obj.push(2);
obj.print();
/*
console.log(obj.getMin());
console.log(obj.getTop());
obj.pop();
console.log(obj.getMin());
console.log(obj.getTop());
*/