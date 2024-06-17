function daily_temperatures(array) {
    let res = new Array(array.length).fill(0);
    let stack = [];
    for(let i=0; i<array.length; i++) {
        while(stack.length !== 0 && stack[stack.length - 1][1] < array[i]) {
            const [idx, val] = stack.pop();
            res[idx] = i - idx;
        }
        stack.push([i, array[i]]);
    }
    console.log(res);
}

daily_temperatures([73,74,75,71,69,72,76,73]);