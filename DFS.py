# DFS function
def dfs(graph, start):
    visited = set() # to keep track of visited nodes
    stack = [start] # to keep track of nodes to be visited
    
    while stack:
        vertex = stack.pop() # get the last node added to stack
        if vertex not in visited:
            visited.add(vertex)
            stack.extend(graph[vertex] - visited) # add unvisited neighbors to stack
    
    return visited
#In the above code, graph is a dictionary representing the graph, where the keys are the nodes and the values are sets of adjacent nodes. start is the starting node from which we want to perform the DFS. The function returns the set of all visited nodes.

#Here's an example of how to use the function with a sample graph:

# Example usage
graph = {'A': set(['B', 'C']),
         'B': set(['A', 'D', 'E']),
         'C': set(['A', 'F']),
         'D': set(['B']),
         'E': set(['B', 'F']),
         'F': set(['C', 'E'])}

print(dfs(graph, 'A'))
# Output: {'A', 'B', 'E', 'F', 'C', 'D'}
#In this example, the graph is represented by a dictionary where node 'A' is connected to nodes 'B' and 'C', node 'B' is connected to nodes 'A', 'D', and 'E', and so on. The DFS is performed starting from node 'A', and the resulting set of visited nodes is printed.
