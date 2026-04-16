class Solution:
    def isPalindrome(self, s: str) -> bool:
        return s == s[::-1]
    def partition(self, s: str) -> List[List[str]]:
        res = []
        cur = []
        def dfs(start):
            if start == len(s):
                res.append(cur.copy())
                return
            for end in range(start+1, len(s) +1):
                if self.isPalindrome(s[start:end]):
                    cur.append(s[start:end])
                    dfs(end)
                    cur.pop()

        dfs(0)
        return res
            
            