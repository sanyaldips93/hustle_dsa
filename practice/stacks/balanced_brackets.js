function balanced_brackets(str) {
    const hash = {')' : '(', ']' : '[', '}' : '{'};
    const stack = [];
    for(const ele of str) {
        // console.log(ele);
        if(ele in hash) {
            if(stack.length !== 0 && stack[stack.length - 1] === hash[ele]) {
                stack.pop();
            } else {
                return false;
            }
        } else {
            stack.push(ele);
        }
    }
    return stack.length !== 0 ? false : true;
}

console.log(balanced_brackets('({[]})'));