"""Q. Design a "Graph" class that represent a Graph where edges 
are represented as {Node1: (Node2, Weight1), Node2: (Node3, Weight2)}"""

class Graph:
    def __init__(self, no_of_nodes):
        # Data members
        self.No_of_node = no_of_nodes
        self.gph = dict()

    def add_edge(self, node1, node2, weight=1):
        if node1 in self.gph.keys():
            newval = (self.gph[node1],(node2,weight))
            self.gph[node1] = newval
        else:
            self.gph[node1] = (node2,weight)
        
    def printGr(self):
        print(self.gph)

g = Graph(4)

g.add_edge(1, 2, 5)
g.add_edge(2, 3, 3)
g.add_edge(3, 4, 6)
g.add_edge(4, 1, 4)
g.add_edge(2, 4, 2)
g.printGr()

# Another test case
g = Graph(5)
g.add_edge(0,1,2)
g.add_edge(1,2,3)
g.add_edge(2,4,7)
g.add_edge(4,1,5)
g.add_edge(3,1,8)
g.add_edge(3,0,6)
g.printGr()


# Directed graph

g = Graph(4)

g.add_edge(0,1,5)
g.add_edge(1,2,4)
g.add_edge(0,2,2)
g.add_edge(2,0,3)
g.add_edge(2,3,3)
g.add_edge(1,3,3)

g.printGr()