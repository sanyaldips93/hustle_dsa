function reverse_polish_notation(array) {
    let stack = [];
    for(const ele of array) {
        if(ele === '+') {
            const a = parseInt(stack.pop());
            const b = parseInt(stack.pop());
            stack.push(a+b);
        } else if(ele === '-') {
            const a = parseInt(stack.pop());
            const b = parseInt(stack.pop());
            stack.push(b-a);
        } else if(ele === '*') {
            const a = parseInt(stack.pop());
            const b = parseInt(stack.pop());
            stack.push(a*b);
        } else if(ele === '/') {
            const a = parseInt(stack.pop());
            const b = parseInt(stack.pop());
            stack.push(Math.trunc(b/a));
        } else {
            stack.push(ele);
        }
    }
    return stack[0];
}

console.log(reverse_polish_notation(["10","6","9","3","+","-11","*","/","*","17","+","5","+"]));