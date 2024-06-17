function trap_rain_water(array) {
    // create a max left array by going through the array once from left to right;
    let maxLeft = 0;
    const maxLArr = [];
    for(let i=0; i<array.length; i++) {
        maxLeft = Math.max(maxLeft, array[i]);
        maxLArr[i] = maxLeft;
    }
    // create a max right array by going through the array once from right to left;
    let maxRight = 0;
    const maxRArr = [];
    for(let i=array.length-1; i>=0; i--) {
        maxRight = Math.max(maxRight, array[i]);
        maxRArr[i] = maxRight;
    }
    // create a min(l, r) for each cell / idx.
    // calculate the amount of water that can be trapped at this index.
    let res = 0;
    for(let i=0; i<array.length; i++) {
        res += Math.min(maxLArr[i], maxRArr[i]) - array[i];
    }
    console.log(res);
}

trap_rain_water([0,1,0,2,1,0,1,3,2,1,2,1]);

// Using two pointers

function trap_rw_tp(array) {
    let res = 0;
    let l = 0;
    let r = array.length - 1;
    let maxLeft = array[0];
    let maxRight = array[array.length-1];

    while(l < r) {
        if(maxLeft < maxRight) {
            l += 1;
            maxLeft = Math.max(maxLeft, array[l]); // if the current height is 4, and maxheight uptil now is 3, 
            // then next part will give negative result.
            // hence update the maxleft and then subtract it, the least case will always be 0;
            res += maxLeft - array[l];
        } else {
            r -= 1;
            maxRight = Math.max(maxRight, array[r]); // if the current height is 4, and maxheight uptil now is 3, 
            // then next part will give negative result.
            // hence update the maxleft and then subtract it, the least case will always be 0;
            res += maxRight - array[r];
        }
    }
    console.log(res);
}

trap_rw_tp([0,1,0,2,1,0,1,3,2,1,2,1]);