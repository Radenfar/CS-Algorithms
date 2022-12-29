class Graph():
    def __init__(self, vertices):
        self.__vertices = vertices
        self.graph = [[0 for column in range(vertices)]
                      for row in range(vertices)]
 
    def printSolution(self, dist):
        print("Vertex \t Distance from Source")
        for node in range(self.__vertices):
            print(node, "\t\t", dist[node])
 
    def minDistance(self, dist, sptSet):
        min = 1e7
        for v in range(self.__vertices):
            if dist[v] < min and sptSet[v] == False:
                min = dist[v]
                min_index = v
        return min_index

    def dijkstra(self, src):
        dist = [1e7] * self.__vertices
        dist[src] = 0
        sptSet = [False] * self.__vertices
        for cout in range(self.__vertices):
            u = self.minDistance(dist, sptSet)
            sptSet[u] = True
            for v in range(self.__vertices):
                if (self.graph[u][v] > 0 and
                   sptSet[v] == False and
                   dist[v] > dist[u] + self.graph[u][v]):
                    dist[v] = dist[u] + self.graph[u][v]
        self.printSolution(dist)
 
#Main
g = Graph(9)
g.graph = [[0, 4, 0, 0, 0, 0, 0, 8, 0],
           [4, 0, 8, 0, 0, 0, 0, 11, 0],
           [0, 8, 0, 7, 0, 4, 0, 0, 2],
           [0, 0, 7, 0, 9, 14, 0, 0, 0],
           [0, 0, 0, 9, 0, 10, 0, 0, 0],
           [0, 0, 4, 14, 10, 0, 2, 0, 0],
           [0, 0, 0, 0, 0, 2, 0, 1, 6],
           [8, 11, 0, 0, 0, 0, 1, 0, 7],
           [0, 0, 2, 0, 0, 0, 6, 7, 0]
           ]
 
'''
In the graph example, each row down is a vertex and if there is a number, that is connected to that index going column-wise
SO:
Vertex 0 is connected to 1 and 7 with weights of 4 and 8 respectively etc.
'''

g.dijkstra(0)