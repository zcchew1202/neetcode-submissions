from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]: 
        groups = defaultdict(list)
        for s in strs:
            s_count = [0] * 26
            for c in s:
                s_count[ord(c)-ord('a')] += 1
            groups[tuple(s_count)].append(s)
        print(groups)
        return list(groups.values())  

