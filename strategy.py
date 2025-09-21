"""
My strategy class
"""

from tyre import tyreSets

class Strategy:

    #initialiser
    def __init__(self, pitLaps, tyreOrder):
        
        self.pitLaps = pitLaps
        self.tyreOrder = [tyreSets[t] for t in tyreOrder]


    #create a text representation of this strategy
    def __repr__(self):
        
        return f"Strategy(pit laps={self.pitLaps}, tyres={[t.name for t in self.tyreOrder]})"
