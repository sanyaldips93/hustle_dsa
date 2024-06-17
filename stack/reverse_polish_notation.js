// Time - O(n), Memory - O(n)
var evalRPN = function(tokens) {
    const stack = [];
    for(const token of tokens) {
        if(token === '+') {
            const a = stack.pop();
            const b = stack.pop();
            stack.push(a+b);
        } else if(token === '-') {
            const a = stack.pop();
            const b = stack.pop();
            stack.push(b-a);
        } else if(token === '*') {
            const a = stack.pop();
            const b = stack.pop();
            stack.push(a*b);
        } else if(token === '/') {
            const a = stack.pop();
            const b = stack.pop();
            stack.push(Math.trunc(b/a));
        } else {
            stack.push(Number(token));
        }
    }
    return stack[0];
};

console.log(evalRPN(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]));