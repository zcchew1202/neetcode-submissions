from collections import Counter
class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if not s or not t or len(s) < len(t):
            return ''
        countS = defaultdict(int)
        countT = Counter(t)
        print(countT)
        l = 0
        res, res_len = '', float('inf')
        have, need = 0, len(countT)
        for r in range(len(s)):
            countS[s[r]] += 1
            if s[r] in countT and countS[s[r]] == countT[s[r]]:
                have += 1
            while have == need:
                if r - l + 1 < res_len:
                    res = s[l:r+1]
                    res_len = r - l + 1
                countS[s[l]] -= 1
                if s[l] in countT and countS[s[l]] < countT[s[l]]:
                    have -= 1

                l += 1
        return res if res_len != float('inf') else ''