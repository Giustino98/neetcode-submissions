from collections import defaultdict, deque

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        adiac_map = defaultdict(list)
        indegree = [0] * numCourses
        q = deque()
        course_attended = 0

        for elem in prerequisites:
            adiac_map[elem[1]].append(elem[0])
            indegree[elem[0]] += 1

        for idx,elem in enumerate(indegree):
            if elem == 0: q.append(idx)    #aggiungo l'indice perchè è l'identificativo del corso

        while q:
            for _ in range(len(q)):
                course = q.popleft()
                course_attended += 1
                for elem in adiac_map[course]:
                    indegree[elem] -= 1
                    if indegree[elem] == 0: q.append(elem)
        return course_attended == numCourses


        

        