class Solution:
    def isPalindrome(self, s: str) -> bool:
        trimmed = ''.join(filter(str.isalnum, s)).lower()
        print(trimmed)
        left, right = 0, len(trimmed)-1
        while left < right:
            if trimmed[left] != trimmed[right]:
                return False
            left += 1
            right -= 1
        return True
