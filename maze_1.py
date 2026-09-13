import sys


class NODE:
    def __init__(self, state, parent, action):
        self.action = action
        self.state = state
        self.parent = parent


# The path cost can be found later


# Class for StackFrontier    , which is a data structure that represents a stack of nodes in a search algorithm. It has methods to add nodes, check if a state is already in the stack, check if the stack is empty, and remove the last node from the stack.
# It represents a last-in-first-out (LIFO) structure, where the most recently added node is the first one to be removed. This is useful in depth-first search algorithms, where we want to explore the most recent path before backtracking to previous paths.
class StackFrontier:
    def __init__(self):
        self.frontier = []

    def add(self, node):
        self.frontier.append(node)

    def contains_state(self, state):
        return any(node.state == state for node in self.frontier)

    def empty(self):
        return len(self.frontier) == 0

    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[
                -1
            ]  # removed the last item of the list and returned it
            self.frontier = self.frontier[:-1]
            return node


# Class for QueueFrontier, which is a data structure that represents a queue of nodes in a search algorithm. It inherits from the StackFrontier class and overrides the remove method to implement a first-in-first-out (FIFO) structure, where the first node added to the queue is the first one to be removed. This is useful in breadth-first search algorithms, where we want to explore all possible paths at the current depth before moving on to deeper paths.
# It represents a first-in-first-out (FIFO) structure, where the first node added to the queue is the first one to be removed. This is useful in breadth-first search algorithms, where we want to explore all possible paths at the current depth before moving on to deeper paths.


class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[
                0
            ]  # removed the first item of the list and returned it
            self.frontier = self.frontier[1:]
            return node


class MAZE:
    def __init__(self, filename):
        with open(filename) as f:
            contents = f.read()

        if contents.count("A") != 1:
            raise Exception("maze must have exactly one starting point")
        if contents.count("B") != 1:
            raise Exception("maze must have exactly one goal")

        contents = contents.splitlines()
        self.height = len(contents)
        self.width = max(len(line) for line in contents)

        self.walls = []
        for i in range(self.height):
            row = []
            for j in range(self.width):
                try:
                    if contents[i][j] == "A":
                        self.start = (i, j)
                        row.append(False)
                    elif contents[i][j] == "B":
                        self.goal = (i, j)
                        row.append(False)
                    elif contents[i][j] == " ":
                        row.append(False)
                    else:
                        row.append(True)
                except IndexError:
                    row.append(False)
            self.walls.append(row)
        self.solution = None

    def print(self):
        solution = self.solution[1] if self.solution is not None else None
        print()
        for i in range(self.height):
            for j in range(self.width):
                if (i, j) == self.start:
                    print("A", end="")
                elif (i, j) == self.goal:
                    print("B", end="")
                elif solution is not None and (i, j) in solution:
                    print("*", end="")
                elif self.walls[i][j]:
                    print("█", end="")
                else:
                    print(" ", end="")
            print()
        print()
        
    def neighbors(self, state):
        row, col = state
        candidates = [
            ("up", (row - 1, col)),
            ("down", (row + 1, col)),
            ("left", (row, col - 1)),
            ("right", (row, col + 1)),
        ]
        result = []
        for action, (r, c) in candidates:
            if 0 <= r < self.height and 0 <= c < self.width and not self.walls[r][c]:
                result.append((action, (r, c)))
        return result
    def solve(self):
         #Finds a solution to the maze, if one exists.
         
         #Keep track of number of states explored
         self.num_explored = 0
         
         #Initialize the frontier to just the starting position
         start = NODE(state=self.start, parent=None, action=None)
         frontier = StackFrontier()
         frontier.add(start)
         
         #Initialize an empty explored set
         self.explored = set()
         
         #Keep looping until solution found
         while True:
             #If nothing left in frontier, then no path
             if frontier.empty():
                 raise Exception("no solution")
             
             #Choose a node from the frontier
             node = frontier.remove()
             self.num_explored += 1
             
             #If node is the goal, then we have a solution
             if node.state == self.goal:
                 actions = []
                 cells = []
                 while node.parent is not None:
                     actions.append(node.action)
                     cells.append(node.state)
                     node = node.parent
                 actions.reverse()
                 cells.reverse()
                 self.solution = (actions, cells)
                 return
             
             #Mark node as explored
             self.explored.add(node.state)
             
             #Add neighbors to frontier
             for action, state in self.neighbors(node.state):
                 if not frontier.contains_state(state) and state not in self.explored:
                     child = NODE(state=state, parent=node, action=action)
                     frontier.add(child)
                     
if __name__ == "__main__":

    # Check command-line arguments
    if len(sys.argv) != 2:
        sys.exit("Usage: python maze.py maze.txt")

    # Create the maze
    maze = MAZE(sys.argv[1])

    # Print the original maze
    print("Maze:")
    maze.print()

    # Solve the maze
    print("Solving...")
    maze.solve()

    # Print number of states explored
    print("States Explored:", maze.num_explored)

    # Print the solution
    print("Solution:")
    maze.print()