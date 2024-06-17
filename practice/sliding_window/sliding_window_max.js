function sliding_window_max(array, k) {
    const q = [];
    const res = [];
    let l = 0;
    let r = 0;

    while(r < array.length) {
        while(q.length && array[q[q.length - 1]] < array[r]) {
            q.pop();
        }
        q.push(r);
        if(l > q[0]) {
            q.shift();
            // l += 1;
        }
        if(r + 1 >= k) {
            res.push(array[q[0]]);
            l += 1;
        }
        r += 1;
    }

    return res;
}

console.log(sliding_window_max([1,3,-1,-3,5,4,6,7], 3));