function best_time(array) {
    let l = 0;
    let r = 1;
    let maxP = 0;

    while(r < array.length) {
        if(array[l] < array[r]) {
            const profit = array[r] - array[l];
            maxP = Math.max(profit, maxP);
        } else {
            l = r;
        }
        r += 1;
    }

    console.log(maxP);
}


best_time([1,4,0,6,5,0,3]);