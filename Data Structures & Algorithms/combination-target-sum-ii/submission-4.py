class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        # each candidate can only be chosen 1x
        res = []
        candidates.sort()
        def dfs(i, choices, total):
            if total == target:
                res.append(choices.copy())
                return
            if total > target or i == len(candidates) :
                return
            choices.append(candidates[i])
            dfs(i+1, choices, total + candidates[i])
            choices.pop()
            while i + 1 < len(candidates) and candidates[i] == candidates[i+1]:
                i += 1
            dfs(i + 1, choices, total)
        dfs(0, [], 0)
        return res
        
