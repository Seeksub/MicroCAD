# from .geometrical_solver import *
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

    def __init__(self, pid=None, x=None, y=None):
        self.x = x
        self.y = y
        if x is not None and y is not None:
            self.points = [[pid, [x, y]], ]

    def addPoint(self, pid, x, y):
        self.points.append([pid, [x, y]])

    def getSetOfPoints(self):
        return self.points

    def deletePoint(self):
        ...

    def movePoint(self):
        ...
    # def findPoint(self, x_pos, y_pos):
    #     for x, val in self.points:
    #         if x_pos not in val[0] and y_pos not in val[1]:
    #             return False
    #         else:
    #             return True
    # def nearPoint(self, x_pos, y_pos):
    #     for x, val in self.points:
    #         if math.fabs(x_pos - val[0]) < 10 and math.fabs(y_pos - val[1]):
    #             return val


class Line:
    lines = []

    def __init__(self, lid=None, x1=None, y1=None, x2=None, y2=None):
        if x1 is not None and x2 is not None and y1 is not None and y2 is not None:
            self.lines = [[lid, [x1, y1, x2, y2]], ]

    def addLine(self, lid, x1, y1, x2, y2):
        # self.pointA.addPoint(x1, y1)
        # self.pointB.addPoint(x2, y2)
        self.lines.append([lid, [x1, y1, x2, y2]])

    def getSetOfLines(self):
        return self.lines

    def deleteLine(self,):
        ...

    def moveLine(self,):
        ...




