# from .geometrical_solver import *
#object structures


class Point:
    points = []
    geometry_constraint = []
    object_constraint = []#check same var for Line class

    def __init__(self, pid=None, x=None, y=None):
        self.x = x
        self.y = y
        if x is not None and y is not None:
            self.points = [[pid, x, y], ]
            self.geometry_constraint = [[pid, 0, 0, 0], ]
    def addPoint(self, pid, x, y):
        self.points.append([pid, x, y])
        self.geometry_constraint.append([pid, 0, 0])

    def getSetOfPoints(self):
        return self.points

    def deletePoint(self, point):
        for i, x in enumerate(self.points):
            if x[0] == point[0]:
                del(self.points[i])

    def changePointCoords(self, point, x, y):
        for i, x in enumerate(self.points):
            if x[0] == point[0]:
                self.points[i][1] = x
                self.points[i][2] = y

    def getPointConstraint(self, point):
        for x in self.geometry_constraint:
            if x[0] == point[0]:
                return x
    def addPointConstraint(self, point, constraint):
        for i, x in enumerate(self.geometry_constraint):
            if x[0] == point[0]:
                self.geometry_constraint[i][constraint] = 1
                self.object_constraint.append([point, constraint])

    def isEventObject(self, point):
        for x in self.points:
            if x[0] == point[0]:
                return True
        return False

class Line:
    lines = []
    geometry_constraint = []#index1-fixed start point, index2- fixed end point, index3-parallelism
    object_constraint = []#[[lid,constaint_index], ]

    def __init__(self, lid=None, x1=None, y1=None, x2=None, y2=None):
        if x1 is not None and x2 is not None and y1 is not None and y2 is not None:
            self.lines = [[lid, x1, y1, x2, y2], ]
            self.geometry_constraint = [[lid, 0, 0, 0, 0, 0, 0, 0, 0, 0], ]

    def addLine(self, lid, x1, y1, x2, y2):
        self.lines.append([lid, x1, y1, x2, y2])
        self.geometry_constraint.append([lid, 0, 0, 0, 0, 0, 0, 0, 0, 0])

    def getSetOfLines(self):
        return self.lines

    def deleteLine(self, line):
        for i, x in enumerate(self.lines):
            if x[0] == line[0]:
                del(self.lines[i])
                del(self.geometry_constraint[i])

    def getLineCoords(self, line):
        for x in self.lines:
            if x[0] == line[0]:
                return x

    def changeLineCoords(self, line, x1, y1, x2, y2):
        for i, x in enumerate(self.lines):
            if x[0] == line[0]:
                self.lines[i][1] = x1
                self.lines[i][2] = y1
                self.lines[i][3] = x2
                self.lines[i][4] = y2

    def getLineConstraint(self, line):
        for x in self.geometry_constraint:
            if x[0] == line[0]:
                return x
    def addLineConstraint(self, line, constraint):
        for i, x in enumerate(self.geometry_constraint):
            if x[0] == line[0]:
                self.geometry_constraint[i][constraint] = 1
                self.object_constraint.append([line, constraint])

    def isEventObject(self, line):
        for x in self.lines:
            if x[0] == line[0]:
                return True
        return False

    def printdata(self, line):
        for i, x in enumerate(self.lines):
            if x[0] == line[0]:
                print(self.lines[i])
                print(self.geometry_constraint[i])


