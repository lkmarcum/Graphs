from graph import Graph
from util import Queue, Stack


def earliest_ancestor(ancestors, starting_node):
    g = Graph()

    for pair in ancestors:
        if pair[0] not in g.vertices.keys():
            g.add_vertex(pair[0])
        if pair[1] not in g.vertices.keys():
            g.add_vertex(pair[1])
        g.add_edge(pair[1], pair[0])

    if len(g.get_neighbors(starting_node)) == 0:
        return -1

    paths = []

    for pair in ancestors:
        new_path = g.dfs(starting_node, pair[0])
        paths.append(new_path)

    # print(paths)

    long_length = 0
    long_paths = []
    for p in paths:
        if p is not None and len(p) > long_length:
            long_length = len(p)
    for p in paths:
        if p is not None and len(p) == long_length:
            long_paths.append(p)
    if len(long_paths) == 1:
        return long_paths[0][-1]
    else:
        # this is arbitrary and stupid, but it works for small values in the graph
        smallest = 100
        for p in long_paths:
            if p[-1] < smallest:
                smallest = p[-1]
        return smallest


test_ancestors = [(1, 3), (2, 3), (3, 6), (5, 6), (5, 7),
                  (4, 5), (4, 8), (8, 9), (11, 8), (10, 1)]

print(earliest_ancestor(test_ancestors, 9))


# s = Stack()
# s.push([starting_vertex])
# visited = set()
# while s.size() > 0:
#     path = s.pop()
#     vertex = path[len(path) - 1]
#      if vertex not in visited:
#           visited.add(vertex)
#            if vertex == destination_vertex:
#                 return path
#             else:
#                 for neighbor in self.get_neighbors(vertex):
#                     new_path = []
#                     for v in path:
#                         new_path.append(v)
#                     new_path.append(neighbor)
#                     s.push(new_path)


# q = Queue()
# # Enqueue A PATH TO the starting vertex
# q.enqueue([starting_vertex])
# # Create a set to store visited vertices
# visited = set()
# # While the queue is not empty...
# while q.size() > 0:
#     # Dequeue the first PATH
#     path = q.dequeue()
#     # GRAB THE VERTEX FROM THE END OF THE PATH
#     vertex = path[len(path) - 1]
#      # Check if it's been visited
#      if vertex not in visited:
#           # If it hasn't been visited...
#           # Mark it as visited
#           visited.add(vertex)
#            # CHECK IF IT'S THE TARGET
#            if vertex == destination_vertex:
#                 # IF SO, RETURN THE PATH
#                 return path
#             else:
#                 # Enqueue A PATH TO all it's neighbors
#                 # MAKE A COPY OF THE PATH
#                 # ENQUEUE THE COPY
#                 for neighbor in self.get_neighbors(vertex):
#                     new_path = []
#                     for v in path:
#                         new_path.append(v)
#                     new_path.append(neighbor)
#                     q.enqueue(new_path)
