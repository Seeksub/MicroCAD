#geometric constraint solver (GCS)
class GCSolver():

    #points
    def concidenceOfPoints(self, x1, y1, x2, y2):
        ...
    def distanceBtwPoints(self, x1, y1, x2, y2):
        ...

    #lines
    def parallelismOfLines(self, L1, L2):
        ...

    def perpendicularityOfLines(self, L1, L2):
        ...

    def angleBtwLines(self, L1, L2):
        ...

    def horizontalOfLine(self, L):
        ...

    def verticalOfLine(self, L):
        ...

    #combo
    def affiliationOFLinePoint(self, L, x, y):
        ...
