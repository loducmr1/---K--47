graph = {
    'A':['B' , 'C' , 'D'],
    'B':['A' , 'E' , 'F'],
    'C':['A' , 'G' , 'H'],
    'D':['A' , 'B'],
    'E':['B'],
    'F':['B'],
    'G':['C'],
    'H':['C' , 'D'],
    }
visited = []
queue = []
def bfs(visited,graph,node):
    visited.append(node)
    queue.append(node)
    while queue:
        m = queue.pop(0)
        print(m, end= " ")
        for neighbour in graph[m]:
            if neighbour not in visited:
                visited.append(neighbour)
                queue.append(neighbour)
print("following is the Breadth-First-Search")
bfs(visited,graph,'A')

visited = set()
def DFS(node,visited,graph):
    if node not in visited:
        print(node)
        visited.add(node)
        for i in graph[node]:
            DFS(i,visited,graph)
print("\nfollowing is the Depth-First-Search")
DFS("A",visited,graph)
