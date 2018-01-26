# Point is the class to represent a 2D data point (x, y).

class Point(object):
    def __init__(self, x, y):
        """
        Constructor of Point.
        
        :param x: The x value of the point. 
        :param y: The y value of the point.
        """
        self.x = x
        self.y = y

    def __lt__(self, rhs):
        """
        Sort the point by comparing x first, then y. If both x and y are equal, the left-hand-side point would be the
         smaller one.
        
        :param rhs: The right-hand-side point to compare with. 
        :return: 
        """
        if self.x != rhs.x:
            return self.x < rhs.x
        elif self.y != rhs.y:
            return self.y < rhs.y
        else:
            return True
