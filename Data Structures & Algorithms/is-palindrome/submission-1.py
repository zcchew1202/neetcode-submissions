import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        words = s.split(' ')
        clean_s = ''.join(filter(str.isalnum,s)).lower()
        l, r = 0, len(clean_s) - 1
        while l < r:
            if clean_s[l] != clean_s[r]:
                return False
            l += 1
            r -= 1
        return True
