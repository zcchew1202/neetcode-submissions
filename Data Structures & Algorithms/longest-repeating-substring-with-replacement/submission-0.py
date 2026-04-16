class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count = {}
        l,r = 0,0
        maxLen = 0
        for r in range(len(s)):
            count[s[r]] = count.get(s[r],0) + 1
            length = r-l +1
            if length - max(count.values()) <= k:
                maxLen = max(maxLen, length)
            else:
                count[s[l]] -= 1
                l += 1
        return maxLen
