import sys


class NODE:
    def __init__(self, state, parent, action):
        self.action = action
        self.state = state
        self.parent = parent


# The path cost can be found later

#Class for StackFrontier    , which is a data structure that represents a stack of nodes in a search algorithm. It has methods to add nodes, check if a state is already in the stack, check if the stack is empty, and remove the last node from the stack.
#It represents a last-in-first-out (LIFO) structure, where the most recently added node is the first one to be removed. This is useful in depth-first search algorithms, where we want to explore the most recent path before backtracking to previous paths.
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
            node = self.frontier[-1]#removed the last item of the list and returned it
            self.frontier = self.frontier[:-1]
            return node
        
#Class for QueueFrontier, which is a data structure that represents a queue of nodes in a search algorithm. It inherits from the StackFrontier class and overrides the remove method to implement a first-in-first-out (FIFO) structure, where the first node added to the queue is the first one to be removed. This is useful in breadth-first search algorithms, where we want to explore all possible paths at the current depth before moving on to deeper paths.
#It represents a first-in-first-out (FIFO) structure, where the first node added to the queue is the first one to be removed. This is useful in breadth-first search algorithms, where we want to explore all possible paths at the current depth before moving on to deeper paths.

class QueueFrontier(StackFrontier):
    def remove(self):
        if self.empty():
            raise Exception("empty frontier")
        else:
            node = self.frontier[0]#removed the first item of the list and returned it
            self.frontier = self.frontier[1:]
            return node