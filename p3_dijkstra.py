#https://gist.github.com/econchick/4666413
from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        #self.nodes = defaultdict(list)
        self.distances = {}
    
    def add_node(self, value):
        self.nodes.add(value)

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        #Agar algoritma tau jarak dari node A ke node B, begitu sebaliknya
        self.distances[(from_node,to_node)] = distance
        #self.edges[to_node].append[from_node]
        #self.distances[(from_node, to_node)] = distance

def dijsktra(graph, initial):
    visited = {initial:0}
    path = defaultdict(list)
    #path = {}

    nodes = set(graph.nodes)

    while nodes:
        min_node = None
        for node in nodes:
            if node in visited:
                if min_node is None:
                    min_node = node
                elif visited[node] < visited[min_node]:
                    min_node = node
        
        if min_node is None:
            break
        
        nodes.remove(min_node)
        current_weight = visited[min_node]

        for edge in graph.edges[min_node]:
            weight = current_weight + graph.distances[min_node, edge]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge].append(min_node)
                #path[edge] = min_node
    
    return path
    # return visited, path

g = Graph()

g.add_node('A')
g.add_node('B')
g.add_node('C')
g.add_node('D')
g.add_node('F')

g.add_edge('A','B',7)
g.add_edge('A','C',9)
g.add_edge('A','F',14)
g.add_edge('B','A',7)
g.add_edge('B','C',10)
g.add_edge('B','D',15)
g.add_edge('C','A',9)
g.add_edge('C','B',10)
g.add_edge('C','D',11)
g.add_edge('C','F',2)
g.add_edge('D','B',15)
g.add_edge('D','C',11)
g.add_edge('D','E',6)
g.add_edge('E','D',6)
g.add_edge('E','F',9)
g.add_edge('F','A',14)
g.add_edge('F','C',2)
g.add_edge('F','E',9)

print(dijsktra(g,'A')['E'])