from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = defaultdict(list)
        in_degree = [0] * numCourses

        for dest, src in prerequisites:
            course_map[src].append(dest)
            in_degree[dest] += 1
        print(course_map)
        queue = deque()
        visited = set()
        
        for i, degree in enumerate(in_degree):
            if degree == 0:
                queue.append(i)
        res = []
        courses_taken = 0
        while queue:
            cur = queue.popleft()
            courses_taken += 1
            res.append(cur)
            for neighbor in course_map[cur]:
                in_degree[neighbor] -= 1
                if in_degree[neighbor] == 0:
                    queue.append(neighbor)
        if numCourses != courses_taken:
            return []
        return res

