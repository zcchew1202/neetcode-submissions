from collections import defaultdict, deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        course_map = defaultdict(list[int])
        in_degrees = [0] * numCourses
        for dest, src in prerequisites:
            course_map[src].append(dest)
            in_degrees[dest] += 1
        queue = deque()
        print(course_map)
        print(in_degrees)

        # seed the queue with 0 deps nodes
        for i, degrees in enumerate(in_degrees):
            print(degrees)
            if degrees == 0:
                queue.append(i)
        courses_taken = 0
        while queue:
            print(queue)
            node = queue.popleft()
            courses_taken += 1
            for neighbor in course_map[node]:
                in_degrees[neighbor] -= 1

                if in_degrees[neighbor] == 0:
                    print(neighbor)
                    queue.append(neighbor)
        return courses_taken == numCourses