from heapq import heappop, heappush


class Gereh:  # a class for storing node specifications

    def __init__(self, vertex, weight=0):
        self.vertexNum = vertex
        self.SourceDist = weight

    def __lt__(self, other):  # Defining the this function to improve min heap performance
        return self.SourceDist < other.SourceDist


class Graph:  # Graph class for storing in adjacency matrix

    def __init__(self, edges, n):

        self.adjList = [[] for _ in range(n)]  # making empty adjacency matrix

        for (mabdae, maghsad, andaze) in edges:

            # Initialization adjacency matrix
            self.adjList[mabdae].append((maghsad, andaze))


def Masir(jad, i, Rah):  # A function to register the road map
    if i >= 0:
        Masir(jad, jad[i], Rah)
        Rah.append(i)


def DijkstraDP(graph, source, n):  # Define a algorithm to find the best path

    Relax = []
    heappush(Relax, Gereh(source))  # create a min heap

    infinity = 1000000000  # This number means infinity

    # Initialize the distances of the nodes from the starting node to infinity(Except start node)
    dist = [infinity] * n
    dist[source] = 0

    pedar = [-5] * n   # Initializing the parent node to find the path

    while Relax:

        # To delete the smallest node and put it in the variable Node(object of Gereh class)
        Node = heappop(Relax)
        u = Node.vertexNum

        # relaxing the children of u node
        for (v, weight) in graph.adjList[u]:
            if (dist[u] + weight) < dist[v]:        # Relaxation condition
                dist[v] = dist[u] + weight
                dist[v] = round(dist[v], 3)
                pedar[v] = u
                heappush(Relax, Gereh(v, dist[v]))

    i = 14  # Khabgah Ghadir(14) is destination
    Rah = []
    Masir(pedar, i, Rah)  # calling Masir function for showing best way

    print("masir Shandiz Haji(", source, ")", " be ", "Khabgah Ghadir",  # print the path and distance
          "(", i, "): az tarigh noghat =", Rah, " ~> tool masir =",  dist[i])



if __name__ == '__main__':  # Starting the driver code

    YallHa = [(0, 1, 0.2), (0, 2, 0.2), (0, 3, 0.6), (1, 2, 2.8), (1, 3, 3.9), (2, 3, 0.4), (2, 6, 4.8),     # Determining the source node, destination and edge weight between them
              (3, 4, 3.8), (3, 5, 6.3), (4, 5, 2), (5, 6, 3.8), (5,8, 0.3), (6, 7, 9), (7, 8, 0.1), (7, 11, 8.2),
              (8, 9, 0.2), (8, 12, 7), (9, 10, 1.1), (9, 13, 2), (10, 15, 3.6), (11, 12, 3.6), (12, 13, 2.4), (13, 14, 0.2), (13, 15, 1.8)]

    n = 16  # Number of graph nodes

    graph = Graph(YallHa, n)  # making object from Grafh class

    source = 0  # Shandiz Haji(0) is startin node

    DijkstraDP(graph, source, n)  # calling DijkstraDP function
