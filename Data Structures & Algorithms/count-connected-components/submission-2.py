from collections import defaultdict, deque

class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        adj_map = defaultdict(list)
        visited = set()
        n_components = 0

        # Costruzione del grafo bidirezionale (Impeccabile!)
        for edge in edges:
            adj_map[edge[0]].append(edge[1])
            adj_map[edge[1]].append(edge[0])

        # La BFS deve solo esplorare e marcare tutto ciò che è connesso a 'start_node'
        def bfs(start_node: int):
            q = deque([start_node])
            visited.add(start_node)

            while q:
                node = q.popleft()
                for elem in adj_map[node]:
                    if elem not in visited:
                        visited.add(elem)
                        q.append(elem) # FONDAMENTALE: l'onda continua a propagarsi
        
        # Ciclo su tutti i nodi
        for node in range(n):
            if node not in visited:
                n_components += 1 # Trovata una nuova componente!
                bfs(node)         # "Colora" tutta questa componente
        
        return n_components