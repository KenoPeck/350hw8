
def numGoodPaths(adjList, topoOrder, u, v):
    goodPaths = 0
    pathCounter = {}

    if (adjList[u][0] == 'G'):
        if u not in pathCounter:
            pathCounter[u] = {}
        pathCounter[u][(1,0)] = 1
    elif (adjList[u][0] == 'Y'):
        if u not in pathCounter:
            pathCounter[u] = {}
        pathCounter[u][(0,1)] = 1

    for node in topoOrder:
        if node not in pathCounter:
                continue
        for neighbor in adjList[node][1]:
            if adjList[neighbor][0] == 'G':
                for (greenCount, yellowCount) in pathCounter[node].keys():
                    if neighbor not in pathCounter:
                        pathCounter[neighbor] = {}
                    if (greenCount + 1, yellowCount) in pathCounter[neighbor].keys():
                        pathCounter[neighbor][(greenCount + 1, yellowCount)] += pathCounter[node][(greenCount, yellowCount)]
                    else:
                        pathCounter[neighbor][(greenCount + 1, yellowCount)] = pathCounter[node][(greenCount, yellowCount)]
            elif adjList[neighbor][0] == 'Y':
                for (greenCount, yellowCount) in pathCounter[node].keys():
                    if neighbor not in pathCounter:
                        pathCounter[neighbor] = {}
                    if (greenCount, yellowCount + 1) in pathCounter[neighbor].keys():
                        pathCounter[neighbor][(greenCount, yellowCount + 1)] += pathCounter[node][(greenCount, yellowCount)]
                    else:
                        pathCounter[neighbor][(greenCount, yellowCount + 1)] = pathCounter[node][(greenCount, yellowCount)]
            else:
                for (greenCount, yellowCount) in pathCounter[node].keys():
                    if neighbor not in pathCounter:
                        pathCounter[neighbor] = {}
                    if (greenCount, yellowCount) in pathCounter[neighbor].keys():
                        pathCounter[neighbor][(greenCount, yellowCount)] += pathCounter[node][(greenCount, yellowCount)]
                    else:
                        pathCounter[neighbor][(greenCount, yellowCount)] = pathCounter[node][(greenCount, yellowCount)]
    if v not in pathCounter:
            pathCounter[v] = {}
    for (greenCount, yellowCount) in pathCounter[v].keys():
        if greenCount > yellowCount:
            goodPaths += pathCounter[v][(greenCount, yellowCount)]

    return goodPaths

adjacencyList = {
    'A': ('G', ('B', 'C', 'D')),
    'B': ('Y', ('E', 'F')),
    'C': ('G', ('G', 'H')),
    'D': ('B', ('I', 'J')),
    'E': ('G', ('K', 'L')),
    'F': ('Y', ('M', 'N')),
    'G': ('Y', ('O', 'P')),
    'H': ('B', ('Q', 'R')),
    'I': ('G', ('S', 'T')),
    'J': ('Y', ('U', 'V')),
    'K': ('R', ()),
    'L': ('B', ()),
    'M': ('G', ()),
    'N': ('Y', ()),
    'O': ('G', ()),
    'P': ('B', ()),
    'Q': ('G', ()),
    'R': ('Y', ()),
    'S': ('R', ()),
    'T': ('B', ()),
    'U': ('G', ()),
    'V': ('Y', ())
}
topologicalOrder = ('A', 'B', 'D', 'C', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V')
u = 'C'
v = 'O'
goodPaths = numGoodPaths(adjacencyList, topologicalOrder, u, v)
print(goodPaths)