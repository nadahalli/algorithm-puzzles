graph = {
    7: [11, 8],
    5: [11], 
    3: [8, 10],
    11: [2, 9, 10],
    8: [9],
    
}

colors = {}
finish = {}
time = 0

def dfs_visit(g, node):
    global time
    colors[node] = 'G'
    time += 1
    adj_list = g.get(node, [])
    for neighbor in adj_list:
        if colors[neighbor] == 'W':
            dfs_visit(g, neighbor)
    time += 1
    colors[node] = 'B'
    finish[node] = time

def dfs(g):
    for node, adj_list in g.iteritems():
        colors[node] = 'W'
        for elem in adj_list:
            colors[elem] = 'W'
    for node in g:
        if colors[node] == 'W':
            dfs_visit(g, node)

dfs(graph)

for n, t in sorted(finish.iteritems(), key = lambda x: x[1]):
    print n, t

