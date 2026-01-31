"""
A* Pathfinding Algorithm
-----------------------
This program finds the shortest path
between a start and goal position
using heuristic-based search.

Author: AI Course
"""

from heapq import heappush, heappop


class AStar:
    def __init__(self, grid, start, goal):
        self.grid = grid
        self.start = start
        self.goal = goal
        self.rows = len(grid)
        self.cols = len(grid[0])

    def heuristic(self, node):
        """
        Manhattan distance heuristic
        """
        return abs(node[0] - self.goal[0]) + abs(node[1] - self.goal[1])

    def get_neighbors(self, node):
        neighbors = []
        x, y = node
        directions = [(0,1), (1,0), (0,-1), (-1,0)]

        for dx, dy in directions:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.rows and 0 <= ny < self.cols:
                if self.grid[nx][ny] == 0:
                    neighbors.append((nx, ny))
        return neighbors

    def find_path(self):
        open_set = []
        heappush(open_set, (0, self.start))

        came_from = {}
        g_score = {self.start: 0}

        while open_set:
            _, current = heappop(open_set)

            if current == self.goal:
                return self.reconstruct_path(came_from, current)

            for neighbor in self.get_neighbors(current):
                tentative_g = g_score[current] + 1

                if neighbor not in g_score or tentative_g < g_score[neighbor]:
                    came_from[neighbor] = current
                    g_score[neighbor] = tentative_g
                    f_score = tentative_g + self.heuristic(neighbor)
                    heappush(open_set, (f_score, neighbor))

        return None

    def reconstruct_path(self, came_from, current):
        path = [current]
        while current in came_from:
            current = came_from[current]
            path.append(current)
        path.reverse()
        return path


def main():
    print("A* PATHFINDING ALGORITHM")
    print("------------------------")

    grid = [
        [0, 0, 0, 0, 1],
        [1, 1, 0, 1, 0],
        [0, 0, 0, 0, 0],
        [0, 1, 1, 1, 0]
    ]

    start = (0, 0)
    goal = (3, 4)

    print("\nGrid (0 = walkable, 1 = obstacle):")
    for row in grid:
        print(row)

    print(f"\nStart: {start}")
    print(f"Goal: {goal}")

    astar = AStar(grid, start, goal)
    path = astar.find_path()

    if path:
        print(f"\nPath found with {len(path)} steps:")
        print(path)
        
        # Visualize path
        print("\nPath visualization (* = path, # = obstacle, . = empty):")
        for i in range(len(grid)):
            row_display = []
            for j in range(len(grid[0])):
                if (i, j) in path:
                    row_display.append('*')
                elif grid[i][j] == 1:
                    row_display.append('#')
                else:
                    row_display.append('.')
            print(' '.join(row_display))
    else:
        print("\nNo path found!")


if __name__ == "__main__":
    main()
