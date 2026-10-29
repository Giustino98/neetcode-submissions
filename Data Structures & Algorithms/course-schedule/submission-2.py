from collections import deque, defaultdict
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        courses_map = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()

        for a,b in prerequisites:
            courses_map[b].append(a)
            indegree[a] += 1
        
        for course in range(numCourses):
            if indegree[course] == 0: queue.append(course)
        
        n_courses = 0
        while queue:
            course = queue.popleft()
            n_courses += 1
            for next_course in courses_map[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0: queue.append(next_course)
        
        return n_courses == numCourses
