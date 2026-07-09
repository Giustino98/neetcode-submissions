from collections import defaultdict, deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prereq_map = defaultdict(list)
        indegree = [0] * numCourses
        q = deque()
        courses_attended = 0
        res = []
        
        for elem in prerequisites:
            prereq_map[elem[1]].append(elem[0])
            indegree[elem[0]] += 1
        
        for idx,elem in enumerate(indegree):
            if elem == 0: q.append(idx)

        
        while q:
            for _ in range(len(q)):
                course = q.popleft()
                res.append(course)
                for elem in prereq_map[course]:
                    indegree[elem] -= 1
                    if indegree[elem] == 0:
                        q.append(elem)
        
        return res if len(res) == numCourses else []
                        



        
        

