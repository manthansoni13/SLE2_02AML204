import timeit
from collections import deque

# Initial State: Requires 5 moves to solve
# Represented as a flat tuple where 0 is the empty tile
START_STATE = (
    1, 2, 3,
    0, 4, 6,
    7, 5, 8
)

# Goal State
GOAL_STATE = (
    1, 2, 3,
    4, 5, 6,
    7, 8, 0
)

# Possible sliding directions (row_offset, col_offset)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_neighbors(state):
    neighbors = []
    zero_idx = state.index(0)
    r, c = divmod(zero_idx, 3)

    for dr, dc in MOVES:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            swap_idx = nr * 3 + nc
            new_state = list(state)
            new_state[zero_idx], new_state[swap_idx] = new_state[swap_idx], new_state[zero_idx]
            neighbors.append(tuple(new_state))
    return neighbors

def bfs(start, goal):
    queue = deque([start])
    visited = {start}
    nodes_expanded = 0

    while queue:
        curr = queue.popleft()
        nodes_expanded += 1

        if curr == goal:
            return True, nodes_expanded

        for neighbor in get_neighbors(curr):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)

    return False, nodes_expanded

def dfs(start, goal, max_depth=15):
    # Depth-limited stack to prevent unbounded recursion
    stack = [(start, 0)]
    visited = {start: 0}
    nodes_expanded = 0

    while stack:
        curr, depth = stack.pop()
        nodes_expanded += 1

        if curr == goal:
            return True, nodes_expanded

        if depth < max_depth:
            for neighbor in get_neighbors(curr):
                if neighbor not in visited or depth + 1 < visited[neighbor]:
                    visited[neighbor] = depth + 1
                    stack.append((neighbor, depth + 1))

    return False, nodes_expanded

def run_profiling(runs=5):
    # Setup timers with timeit
    bfs_timer = timeit.Timer(lambda: bfs(START_STATE, GOAL_STATE))
    dfs_timer = timeit.Timer(lambda: dfs(START_STATE, GOAL_STATE))

    # timeit measures total seconds; convert to average milliseconds per run
    avg_bfs_time = (bfs_timer.timeit(number=runs) / runs) * 1000
    avg_dfs_time = (dfs_timer.timeit(number=runs) / runs) * 1000

    # Collect single-run node expansion stats
    bfs_found, bfs_nodes = bfs(START_STATE, GOAL_STATE)
    dfs_found, dfs_nodes = dfs(START_STATE, GOAL_STATE)

    print("================ Profiling Results ================")
    print(f"{'Metric':<25} | {'BFS':<15} | {'DFS':<15}")
    print("-" * 60)
    print(f"{'Nodes Expanded':<25} | {bfs_nodes:<15} | {dfs_nodes:<15}")
    print(f"{'Average Time (ms)':<25} | {avg_bfs_time:<15.4f} | {avg_dfs_time:<15.4f}")
    print(f"{'Target Found':<25} | {str(bfs_found):<15} | {str(dfs_found):<15}")
    print("===================================================")

if __name__ == "__main__":
    run_profiling(runs=5)