function generate_paranthesis(n) {
    let res = [];
    backtrack(0, 0, res, "", n);
    return res;
}

function backtrack(open, close, res, str, n) {
    if(open === n && close === n) {
        res.push(str);
    }
    if(open < n) {
        const newStr = str + "(";
        backtrack(open+1, close, res, newStr, n);
    }
    if(close < open) {
        const newStr = str + ")";
        backtrack(open, close+1, res, newStr, n);
    }
}

console.log(generate_paranthesis(3));