#Adjacency Matrix 

#     v0  v1  v2  v3  v4  v5
# v0

# v1

# v2

# v3

# v4

class Graph:
    def __init__(self,vno):
        self.vertex_coutns=vno
        self.adj_matrix = [ [0]*vno for i in range(vno) ]

    def add_edges(self,u,v,weight=1):
        if 0<=u<self.vertex_coutns and 0<=v<self.vertex_coutns:
            self.adj_matrix[u][v]=weight
            self.adj_matrix[v][u]=weight
        else:
            print("Invalid Vertex")