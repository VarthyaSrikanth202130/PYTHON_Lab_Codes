""" Write a program to represent Graph using Adjaceny Matrix """

class Graph:
    def __init__(self,size) -> None:
        self.Nodesize = size # to track number of the nodes
        # create and initialize matrix with 0 initially
        self.adjMatrix = [[0]*size for i in range(size)] 
    
    def printmatrix(self):
        '''returns the adjacency matrix''' 
        print(self.adjMatrix)
    
    def add_edge(self,edg):
        '''a method that adds the edges to make a graph'''
        edg = list(edg.split(','))
        edg = [int(i) for i in edg]
        if edg[0] == edg[1] :
            print(f"Same vertex {edg[0]} and {edg[1]}")
        
        
        self.adjMatrix[edg[0]][edg[1]] = 1  
        self.adjMatrix[edg[1]][edg[0]] = 1 
    
# driver code                 
no_of_vertices = int(input("Enter no. of vertices or nodes : "))

g = Graph(no_of_vertices)                                           
for i in range(no_of_vertices):
    edge = input(f"Enter edge {i} : ")   
    g.add_edge(edge)
    
g.printmatrix()