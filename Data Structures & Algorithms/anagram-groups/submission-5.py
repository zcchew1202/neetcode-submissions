from collections import Counter
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        count_chars = defaultdict(list)
        for s in strs:
            word_key = [0] * 26
            for c in s:
                word_key[ord(c)-ord('a')] += 1
            count_chars[tuple(word_key)].append(s)
        return [v for v in count_chars.values()]
            

                
                