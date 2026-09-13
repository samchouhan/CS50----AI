import sys

class NODE():
    def __init__(self,state,parent,action):
        self.action = action
        self.state = state
        self.parent = parent
        
        
class StackFrontier():
    def __init__(self):
        self.frontier = []
        
        