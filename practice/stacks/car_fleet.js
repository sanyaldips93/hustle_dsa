function car_fleet(target, position, speed) {
    const array = new Array(position.length);
    for(let i=0; i<position.length; i++) {
        array[i] = [position[i], speed[i]];
    }
    array.sort((a,b) => b[0] - a[0]);
    const stack = [];
    for(let a=0; a<array.length; a++) {
        const [position, speed] = array[a];
        stack.push((target-position)/speed);

        if(stack.length >=2 && stack[stack.length - 1] <= stack[stack.length - 2]) {
            stack.pop();
        }
    }
    return stack.length;
}

console.log(car_fleet(12, [10,8,0,5,3], [2,4,1,1,3]));