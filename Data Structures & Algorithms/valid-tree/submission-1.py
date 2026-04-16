class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        cycle, visited = set(), set()
        edgeMap = defaultdict(list)
        for src, dest in edges:
            edgeMap[src].append(dest)
            edgeMap[dest].append(src)
        def dfs(node, prev):
            if node in cycle:
                return False
            if node in visited:
                return True
            cycle.add(node)
            for nextNode in edgeMap[node]:
                if nextNode == prev:
                    continue
                if not dfs(nextNode, node):
                    return False
            cycle.remove(node)
            visited.add(node)
            return True
        
        return dfs(0,-1) and len(visited) == n