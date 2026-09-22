import sys
from collections import deque

START_STATE = (1, 2, 3, 0, 4, 6, 7, 5, 8)
GOAL_STATE = (1, 2, 3, 4, 5, 6, 7, 8, 0)
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
    while queue:
        curr = queue.popleft()
        if curr == goal:
            return True
        for neighbor in get_neighbors(curr):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
    return False

def dfs(start, goal, max_depth=15):
    stack = [(start, 0)]
    visited = {start: 0}
    while stack:
        curr, depth = stack.pop()
        if curr == goal:
            return True
        if depth < max_depth:
            for neighbor in get_neighbors(curr):
                if neighbor not in visited or depth + 1 < visited[neighbor]:
                    visited[neighbor] = depth + 1
                    stack.append((neighbor, depth + 1))
    return False

if __name__ == "__main__":
    algo = sys.argv[1] if len(sys.argv) > 1 else "bfs"
    if algo == "bfs":
        for _ in range(8000):
            bfs(START_STATE, GOAL_STATE)
    elif algo == "dfs":
        for _ in range(800):
            dfs(START_STATE, GOAL_STATE)