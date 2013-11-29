class Coordinate(object):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def getX(self):
        # Getter method for a Coordinate object's x coordinate.
        # Getter methods are better practice than just accessing an attribute directly
        return self.x

    def getY(self):
        # Getter method for a Coordinate object's y coordinate
        return self.y

    def __str__(self):
        return '<' + str(self.getX()) + ',' + str(self.getY()) + '>'
    
    #Adding __eq__ and __repr__
    def __eq__(self,other):
        return self.x==other.x and self.y==other.y
            
    def __repr__(self):
        return 'Coordinate('+str(self.getX())+', '+str(self.getY())+')'
        
c1 = Coordinate(3,4)
c2 = Coordinate(3,4)
print c1 == c2