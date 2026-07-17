from collections import deque
def water_jug(capacity1, capacity2, target):
    queue = deque()
    visited = set()
    queue.append((0, 0, []))  # (jug1, jug2, path)
    while queue:
        jug1, jug2, path = queue.popleft()
        if (jug1, jug2) in visited:
            continue
        visited.add((jug1, jug2))
        path = path + [(jug1, jug2)]
        if jug1 == target or jug2 == target:
            print("Solution:")
            for state in path:
                print(state)
            return
        next_states = [
            (capacity1, jug2),                     
            (jug1, capacity2),                     
            (0, jug2),                             
            (jug1, 0),                             
            (jug1 - min(jug1, capacity2 - jug2),
             jug2 + min(jug1, capacity2 - jug2)),  
            (jug1 + min(jug2, capacity1 - jug1),
             jug2 - min(jug2, capacity1 - jug1))   
        ]
        for state in next_states:
            if state not in visited:
                queue.append((state[0], state[1], path))
    print("No solution exists.")
capacity1 = 4
capacity2 = 3
target = 2
water_jug(capacity1, capacity2, target)