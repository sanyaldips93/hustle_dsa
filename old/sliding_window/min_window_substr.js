var minWindow = function(s, t) {
    if(t==="" || t.length>s.length) return ""
    const ch = {};
    const sh = {};
    for(const c of t){
        if(c in ch) ch[c] += 1;
        else ch[c] = 1;
    }
    const need = Object.keys(ch).length;
    let have = 0;
    let l = 0;
    let r = 0;
    let res = Number.MAX_SAFE_INTEGER;
    let arr = [-1, -1];
    while(r < s.length) {
        let chr = s[r];
        if(chr in sh) sh[chr] += 1;
        else sh[chr] = 1;
        if(chr in ch && sh[chr] === ch[chr]) {
            have += 1;
        }
        while(have === need) {
            let chl = s[l];
            if(r-l+1 < res) {
                res = r-l+1;
                arr = [l,r];
            }
            sh[chl] -= 1;
            if(chl in ch && ch[chl] > sh[chl]) {
                have -= 1;
            }
            l += 1;
        }
        r += 1;
    }
    if(res !== Number.MAX_SAFE_INTEGER) {
        return s.substring(arr[0], arr[1]+1);
    }
    return "";
};

console.log(minWindow('BCKZAOXBEA', 'AA'));