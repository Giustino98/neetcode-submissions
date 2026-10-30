from collections import deque, defaultdict
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        courses_map = defaultdict(list)
        indegree = defaultdict(int)
        queue = deque()
        res = []

        for a,b in prerequisites:
            courses_map[b].append(a)
            indegree[a] += 1
        
        for course in range(numCourses):
            if indegree[course] == 0: queue.append(course)
        
        while queue:
            course = queue.popleft()
            res.append(course)
            for next_course in courses_map[course]:
                indegree[next_course] -= 1
                if indegree[next_course] == 0: queue.append(next_course)
            
        return res if len(res) == numCourses else []