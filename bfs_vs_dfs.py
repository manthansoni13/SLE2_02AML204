import timeit
from collections import deque

# Simple directed graph with 10 nodes (0 to 9)
GRAPH = {
    0: [1, 2],
    1: [0, 3, 4],
    2: [0, 5, 6],
    3: [1, 7],
    4: [1, 8],
    5: [2],
    6: [2, 9],
    7: [3],
    8: [4],
    9: [6]
}

START_NODE = 0
TARGET_NODE = 9

def bfs(graph, start, target):
    visited = set()
    queue = deque([start])
    visited.add(start)
    nodes_expanded = 0

    while queue:
        curr = queue.popleft()
        nodes_expanded += 1

        if curr == target:
            return True, nodes_expanded

        for neighbor in graph.get(curr, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False, nodes_expanded

def dfs(graph, start, target):
    visited = set()
    stack = [start]
    visited.add(start)
    nodes_expanded = 0

    while stack:
        curr = stack.pop()
        nodes_expanded += 1

        if curr == target:
            return True, nodes_expanded

        for neighbor in graph.get(curr, []):
            if neighbor not in visited:
                visited.add(neighbor)
                stack.append(neighbor)

    return False, nodes_expanded

if __name__ == "__main__":
    runs = 1000

    # Measure execution time using timeit
    bfs_timer = timeit.Timer(lambda: bfs(GRAPH, START_NODE, TARGET_NODE))
    dfs_timer = timeit.Timer(lambda: dfs(GRAPH, START_NODE, TARGET_NODE))

    # Convert total seconds over 1000 runs to average time in milliseconds
    bfs_avg_time = (bfs_timer.timeit(number=runs) / runs) * 1000
    dfs_avg_time = (dfs_timer.timeit(number=runs) / runs) * 1000

    # Collect single-run node expansion statistics
    bfs_found, bfs_nodes = bfs(GRAPH, START_NODE, TARGET_NODE)
    dfs_found, dfs_nodes = dfs(GRAPH, START_NODE, TARGET_NODE)

    print("================ Profiling Results ================")
    print(f"{'Metric':<25} | {'BFS':<12} | {'DFS':<12}")
    print("-" * 55)
    print(f"{'Nodes Expanded':<25} | {bfs_nodes:<12} | {dfs_nodes:<12}")
    print(f"{'Average Time (ms)':<25} | {bfs_avg_time:<12.6f} | {dfs_avg_time:<12.6f}")
    print(f"{'Target Found':<25} | {str(bfs_found):<12} | {str(dfs_found):<12}")
    print("===================================================")