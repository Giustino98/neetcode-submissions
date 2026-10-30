from collections import deque, defaultdict
class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_list = defaultdict(list)
        visited = set()

        n_connected = 0

        for a,b in edges:
            adj_list[a].append(b)
            adj_list[b].append(a)

        def bfs(node):
            queue = deque()
            queue.append(node)
            visited.add(node)
            while queue:
                node = queue.popleft()
                for next_node in adj_list[node]:
                    if next_node not in visited:
                        visited.add(next_node)
                        queue.append(next_node)
        
        for node in range(n):
            if node not in visited:
                n_connected +=1
                bfs(node)
        
        return n_connected