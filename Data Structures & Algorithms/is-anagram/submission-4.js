class Solution {
    /**
     * @param {string} s
     * @param {string} t
     * @return {boolean}
     */
    countChars(s) {
        const counts = {}
        for (let i=0; i < s.length; i++) {
            if (!counts[s[i]]) {
                counts[s[i]] = 1

            } else {
                counts[s[i]] += 1
            }
        }
        console.log(counts)
        return counts
    }
    isAnagram(s, t) {
        if (s.length !== t.length) {
            return false;
        }
        const countS = this.countChars(s);
        const countT = this.countChars(t);
        for (const key in countS) {
            if (countS[key] !== countT[key]){
                return false;
            }
        }
        return true;
    }
}
