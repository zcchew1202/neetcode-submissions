from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(s) < len(t):
            return ''
        if t == '':
            return t
        if s == t:
            return s
        countT = Counter(t)
        window = defaultdict(int)
        have, need = 0, len(countT)
        l = 0
        res, resLen = [-1,-1], float('infinity')
        for r in range(len(s)):
            c = s[r]
            window[c] += 1

            if c in countT and window[c] == countT[c]:
                have += 1
            while have == need:
                # update res
                if (r-l+1) < resLen:
                    res = [l,r]
                    resLen = r-l+1
                # shrink window
                oldChar = s[l]
                window[oldChar] -= 1
                if oldChar in countT and window[oldChar] < countT[oldChar]:
                    have -= 1
                l += 1
        l,r = res
        return s[l:r+1] if resLen != float('infinity') else ''
            
            
        