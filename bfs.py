def input_graph():
    graph = {}
    n = int(input("Enter the number of nodes: "))
    for i in range(n):
        node = input("Enter node: ")
        neighbours = input(f"Enter neighbors of {node} (space-separated): ").split()
        graph[node] = neighbours
    return graph

# DFS Algorithm
def DFS(graph, node):
    stack = [node]
    visited = []

    print("\nOrder of visited nodes by DFS:", end=" ")

    while stack:
        s = stack.pop()

        if s not in visited:
            visited.append(s)
            print(s, end=" ")

        for neighbour in graph[s]:
            if neighbour not in visited:
                stack.append(neighbour)

# BFS Algorithm
def BFS(graph, node):
    queue = [node]
    visited = [node]

    print("\nOrder of visited nodes by BFS:", end=" ")

    while queue:
        m = queue.pop(0)
        print(m, end=" ")

        for neighbour in graph[m]:
            if neighbour not in visited:
                queue.append(neighbour)
                visited.append(neighbour)

# Main program
graph = input_graph()
start_node = input("\nEnter the starting node: ")

print("\nBFS and DFS Traversals:")
BFS(graph, start_node)
DFS(graph, start_node)
