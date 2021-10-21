from graph import *

g = Graph({1:[2,3], 2:[], 3:[4,5], 4:[], 5:[]})

print("Graph: " + str(g))
print("Cycle? " + str(g.isCyclic()))

g.addEdge(5,1)

print("Graph: " + str(g))
print("Cycle? " + str(g.isCyclic()))
