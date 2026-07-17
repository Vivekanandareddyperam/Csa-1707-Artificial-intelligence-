import heapq
GOAL = (
    (1, 2, 3),
    (4, 5, 6),
    (7, 8, 0)
)
MOVES = [(-1, 0), (1, 0), (0, -1), (0, 1)]
def manhattan(state):
    distance = 0
    for i in range(3):
        for j in range(3):
            value = state[i][j]
            if value != 0:
                goal_row = (value - 1) // 3
                goal_col = (value - 1) % 3
                distance += abs(i - goal_row) + abs(j - goal_col)
    return distance
def find_blank(state):
    for i in range(3):
        for j in range(3):
            if state[i][j] == 0:
                return i, j
def get_neighbors(state):
    x, y = find_blank(state)
    neighbors = []
    for dx, dy in MOVES:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_state = [list(row) for row in state]
            new_state[x][y], new_state[nx][ny] = new_state[nx][ny], new_state[x][y]
            neighbors.append(tuple(tuple(row) for row in new_state))

    return neighbors
def a_star(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start))

    came_from = {}
    cost = {start: 0}

    while pq:
        _, g, current = heapq.heappop(pq)

        if current == GOAL:
            path = []
            while current in came_from:
                path.append(current)
                current = came_from[current]
            path.append(start)
            return path[::-1]

        for neighbor in get_neighbors(current):
            new_cost = g + 1

            if neighbor not in cost or new_cost < cost[neighbor]:
                cost[neighbor] = new_cost
                priority = new_cost + manhattan(neighbor)
                heapq.heappush(pq, (priority, new_cost, neighbor))
                came_from[neighbor] = current
    return None
def print_state(state):
    for row in state:
        print(*row)
    print()
start = (
    (1, 2, 3),
    (4, 0, 6),
    (7, 5, 8)
)
solution = a_star(start)
if solution:
    print(f"Solution found in {len(solution) - 1} moves:\n")
    for step in solution:
        print_state(step)
else:
    print("No solution exists.")