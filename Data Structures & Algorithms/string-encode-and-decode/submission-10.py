class Solution:

    def encode(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        strBuild = ''
        for s in strs:
            strBuild += str(len(s)) + '-' + s
        return strBuild 

    def decode(self, s: str) -> List[str]:
        if len(s) == 0:
            return []
        l = 0 
        r = 0
        res = []
        print(s)
        while l < len(s):
            r = l
            while s[r] != '-':
                r += 1
            # account for multiple digits like 10
            offset = int(s[l:r])
            res.append(s[r+1:r+offset+1])
            l = r+offset+1
            print(res)
        return res
           

        
