function valid_palindrome(string) {
    let first = 0;
    let last = string.length - 1;
    while(first <= last) {
        if(string[first] != string[last]) {
            return 'Not valid palindromes!';
        } else {
            first++;
            last--;
        }
    }
    return 'Valid palindromes!';
}

console.log(valid_palindrome('abbaz'));