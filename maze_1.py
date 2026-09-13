import sys


class NODE:
    def __init__(self, state, parent, action):
        self.action = action
        self.state = state
        self.parent = parent


# The path cost can be found later


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
        
class QueueFrontier(StackFrontier):
