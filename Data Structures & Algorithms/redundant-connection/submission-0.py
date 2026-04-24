from collections import deque, defaultdict
import itertools
class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        adj = defaultdict(list)
        nodes = set(list(itertools.chain.from_iterable(edges)))
        in_degrees = [0] * (len(nodes) + 1)
        
        for src, dest in edges:
            adj[src].append(dest)
            adj[dest].append(src)
            in_degrees[dest] += 1
            in_degrees[src] += 1
        queue = deque()

        for i, degree in enumerate(in_degrees):
            if degree == 1:
                queue.append(i)
        while queue:
            cur = queue.popleft()
            in_degrees[cur] -= 1
            for nei in adj[cur]:
                in_degrees[nei] -= 1
                if in_degrees[nei] == 1:
                    queue.append(nei)
        print(in_degrees)
        for src, dest in reversed(edges):
            if in_degrees[src] >= 2 and in_degrees[dest]:
                return [src,dest]
        return []

            