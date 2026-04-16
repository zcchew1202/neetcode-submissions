class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        visit, cleared = set(), set()
        courseMap = defaultdict(list)
        for course, prereq in prerequisites:
            courseMap[course].append(prereq)
        print(courseMap)
        def dfs(node):
            if node in visit:
                return False
            if node in cleared:
                return True
            visit.add(node)
            for pre in courseMap[node]:
                if not dfs(pre):
                    return False
            visit.remove(node)
            cleared.add(node)
            return True
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
            