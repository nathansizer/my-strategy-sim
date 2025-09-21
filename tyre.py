"""
The Tyre class of my simulation model.
This defines the tyres and each of their properties.
"""

class Tyre:

    #initialiser
    def __init__(self, name, baseOffset, degRate, lifespan):

        self.name = name
        self.baseOffset = baseOffset
        self.degRate = degRate
        self.lifespan = lifespan

    #the modifier of time penalty based on a tyre's age
    def degModifier(self, age):

        return self.baseOffset + (age * self.degRate)

#my pre-defined tyre models for this example
SOFT = Tyre("Soft", 0.0, 0.08, 18)
MEDIUM = Tyre("Medium", 0.15, 0.05, 28)
HARD = Tyre("Hard", 0.45, 0.03, 40)

#now let's put the tyres into a library
tyreSets = {"soft": SOFT, "medium": MEDIUM, "hard": HARD}

    
        
