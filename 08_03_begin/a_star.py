"""
Python Data Structures - A Game-Based Approach
A Star Algorithm maze solver.
Robin Andrews - https://compucademy.net/
Uses a priority queue containing f-values and (i, j) tuples along with dictionaries for
predecessors and g-values.
"""

from helpers import get_path, offsets, is_legal_pos, read_maze
from priority_queue import PriorityQueue


def heuristic(a, b):
    """
    Calculates the Manhattan distance between two pairs of grid coordinates.
    """
    x1, y1 = a
    x2, y2 = b
    return abs(x1 - x2) + abs(y1 - y2)  # abs() = absolute value (non negative)


def a_star(maze, start, goal):
    pq = PriorityQueue()
    pq.put(start, 0)
    predecessors = {start: None}
    g_values = {start: 0}

    while not pq.is_empty():
        current_cell = pq.get()
        # if the current_cell is equal to the goal, return the path
        if current_cell == goal:
            return get_path(predecessors, start, goal)
        # otherwise, go to the directions and find the undiscovered neighbour
        for direction in ["up", "right", "down", "left"]:
            row_offset, col_offset = offsets[direction]
            neighbour = (current_cell[0] + row_offset, current_cell[1] + col_offset)
            # if it's a legal position in the maze and the neighbour is not in the g_values (undiscovered)
            if is_legal_pos(maze, neighbour) and neighbour not in g_values:
                # the g_value of the neighbour is equal to the new cost
                new_cost = g_values[current_cell] + 1
                g_values[neighbour] = new_cost
                # the g_value is equal to the new cost + the heuristic of goal and neighbour
                f_value = new_cost + heuristic(goal, neighbour)
                # Add (neighbour, f_value) to the pq
                pq.put(neighbour, f_value)
                # Update the predecessors so the predecessors for that neighbour is equal to the current_cell
                predecessors[neighbour] = current_cell
                # Putting it in g_values and in predicessors are both equivalent to saying we've discovered this.

        # If we can't find the destination, return None
    return None


if __name__ == "__main__":
    # Test 1
    maze = [[0] * 3 for row in range(3)]
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (0, 1), (0, 2), (1, 2), (2, 2)]

    # Test 2
    maze = read_maze("mazes/mini_maze_bfs.txt")
    for row in maze:
        print(row)
    start_pos = (0, 0)
    goal_pos = (2, 2)
    result = a_star(maze, start_pos, goal_pos)
    assert result == [(0, 0), (1, 0), (1, 1), (1, 2), (2, 2)]

    # Test 3
    maze = read_maze("mazes/mini_maze_bfs.txt")
    start_pos = (0, 0)
    goal_pos = (3, 3)
    result = a_star(maze, start_pos, goal_pos)
    assert result is None
