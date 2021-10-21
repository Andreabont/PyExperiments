class Graph:
    
    graph = dict()
    nVisited = dict()
    recStack = dict()

    def __init__(self, newGraph):
        self.graph = newGraph
    
    def addEdge(self, node_a, node_b):
        if node_a in self.graph:
            self.graph[node_a].append(node_b)
        else:
            self.graph[node_a] = [node_b]
        if node_b not in self.graph:
            self.graph[node_b] = []
    
    def getNodes(self):
        return list(self.graph.keys())
     
    def getAdjacency(self, node):
        return self.graph[node]
    
    def _isCyclicUtil(self, i):
        
        if not self.nVisited[i]:
            
            self.nVisited[i] = True
            self.recStack[i] = True
            
            for n in self.getAdjacency(i):
                if not self.nVisited[n] and self._isCyclicUtil(n):
                    return True
                elif self.recStack[n]:
                    return True
            
        self.recStack[i] = False
        return False
    
    def isCyclic(self):
        
        self.nVisited = {x: False for x in self.getNodes()}
        self.recStack = {x: False for x in self.getNodes()}
        
        for i in self.getNodes():
            if self._isCyclicUtil(i):
                return True
            
        return False
    
    def __str__(self):
        return str(self.graph)