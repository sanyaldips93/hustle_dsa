function largest_histogram(array) {
    const stack = [];
    let maxArea = 0;
    for(let i=0; i<array.length; i++) {
        let start = i;
        while(stack.length !== 0 && stack[stack.length-1][1] > array[i]) {
            const [idx, h] = stack.pop();
            maxArea = Math.max(maxArea, (i-idx)*h);
            start = idx;
        }
        stack.push([start, array[i]]);
    }
    for(let i=0; i<stack.length; i++) {
        const idx = stack[i][0];
        const h = stack[i][1];
        maxArea = Math.max(maxArea, (array.length-idx)*h);
    }
    console.log(maxArea);
}

largest_histogram([2,1,5,6,2,3]);
