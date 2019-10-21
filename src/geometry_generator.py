#object structures

# class Object():
#     def __init__(self, obj):
#         self.obj_set = [obj,]
#     def addToSet(self, obj):
#         self.obj_set.append(obj)
#
#     ...
import math

class Point:
    points = []

    def __init__(self, x=None, y=None):
        self.x = x
        self.y = y
        if x is not None and y is not None:
            self.points = [[x, y], ]

    def addPoint(self, x, y):
        self.points.append([x, y])

    def getSetOfPoints(self):
        return self.points

    def findPoint(self, x_pos, y_pos):
        for x, val in self.points:
            if x_pos not in val[0] and y_pos not in val[1]:
                return False
            else:
                return True
    def nearPoint(self, x_pos, y_pos):
        for x, val in self.points:
            if math.fabs(x_pos - val[0]) < 10 and math.fabs(y_pos - val[1]):
                return val


class Line:
    lines = []

    def __init__(self, x1=None, y1=None, x2=None, y2=None):
        if x1 is not None and x2 is not None and y1 is not None and y2 is not None:
            self.pointA = Point(x1, y1)
            self.pointB = Point(x2, y2)
            self.lines = [[self.pointA, self.pointB], ]

    def addLine(self, x1, y1, x2, y2):
        self.pointA.addPoint(x1, y1)
        self.pointB.addPoint(x2, y2)
        self.lines.append([self.pointA.getSetOfPoints(), self.pointB.getSetOfPoints()])

    def getSetOfLines(self):
        return self.lines

    def findLine(self, x1, y1, x2, y2):
        ...





