graph = {
    'a': [('b', 2), ('c', 1)],
    'b': [('c', 1)],
    'c': [('a', 9), ('d', 8), ('e', 2)],
    'd': [('a', 3)],
    'e': [('d', 3)]
    }

source = 'c'

def find_min(relaxers, unexplored):
    min_vertex = None
    min_value = float('inf')
    for vertex in relaxers:
        if vertex not in unexplored:
            continue
        if relaxers[vertex] < min_value:
            min_value = relaxers[vertex]
            min_vertex = vertex
    return min_vertex

paths = {}
relaxers = {}
unexplored = []
for vertex in graph:
    unexplored.append(vertex)
    relaxers[vertex] = float('inf')
    paths[vertex] = []

relaxers[source] = 0

while len(unexplored) > 0:
    min_vertex = find_min(relaxers, unexplored)
    min_vertex_dist = relaxers[min_vertex]
    paths[min_vertex] = source
    source = min_vertex
    unexplored.remove(min_vertex)
    adj_list = graph[min_vertex]
    for (adj_vertex, adj_vertex_dist) in adj_list:
        if min_vertex_dist + adj_vertex_dist < relaxers[adj_vertex]:
            relaxers[adj_vertex] = min_vertex_dist + adj_vertex_dist
print paths
print relaxers

dest = 'b'
source = 'c'

path = []
print 'Path cost:',  relaxers[dest]

while (dest != source):    
    path.append(dest)
    dest = paths[dest]
path.append(source)
path.reverse()

print 'Path:', path
