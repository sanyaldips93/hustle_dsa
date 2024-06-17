function product_of_array_except_self(array) {
    const res = new Array(array.length).fill(1);

    let prefix = 1;
    for(let i=0; i<array.length; i++) {
        res[i] = prefix;
        prefix *= array[i];
    }

    let postfix = 1;
    for(let i=array.length-1; i>=0; i--) {
        res[i] *= postfix;
        postfix *= array[i];
    }

    return res;
}

console.log(product_of_array_except_self([1,2,3,4]));