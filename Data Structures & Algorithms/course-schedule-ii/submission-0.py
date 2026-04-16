class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        visiting = set()
        visited = set()
        courseMap = defaultdict(list)
        for course,pre in prerequisites:
            courseMap[course].append(pre)
        output = []
        def dfs(course):
            if course in visited:
                return False
            if course in visiting:
                return True
            visited.add(course)
            for prereq in courseMap[course]:
                if not dfs(prereq):
                    return False
            visited.remove(course)
            visiting.add(course)
            output.append(course)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return []
        return output
            
            
        