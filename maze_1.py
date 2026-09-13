import sys

class NODE():
    def __init__(self,state,parent,action):
        self.action = action
        self.state = state
        self.parent = parent
        
#The path cost can be found later 
        
        
class StackFrontier():
    def __init__(self):
        self.frontier = []
        
        