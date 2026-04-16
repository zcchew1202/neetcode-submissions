class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adjList = defaultdict(list)
        visited = set()
        for src, dest in edges:
            adjList[src].append(dest)
            adjList[dest].append(src)
        def dfs(node):
            if node in visited:
                return 
            visited.add(node)
            for neighbor in adjList[node]:
                dfs(neighbor)
        count = 0
        for i in range(n):
            if i not in visited:
                dfs(i)
                count += 1
        return count