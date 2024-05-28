import sys
sys.path.append("..")

from Geometryczne.CPoint import Point
class FromFile:

    def __init__(self):
        self.pointsTab = []
        self.melodyTab = []
        self.vertexTab = []
        self.guardsTab = []

    def printPoints(self):
        for i in self.pointsTab:
            print(i.x,i.y)

    def printVertexTab(self):
        for i in self.vertexTab:
            print(i)

    def importfromFileProblemOne(self, filename):
        file = open(filename, 'r')
        line = file.readline()
        numberOfVertex = int(line)
        self.vertexTab = [[0 for _ in range(numberOfVertex+2)] for _ in range(numberOfVertex+2)]
        line = file.readline()
        numberOfEdges = int(line)
        for i in range(numberOfEdges):
            line = file.readline()
            edge = line.split(" ")
            edge[0] = int(edge[0])
            edge[1] = int(edge[1])
            self.vertexTab[0][edge[0]] = 1
            self.vertexTab[edge[1]][numberOfVertex+1] = 1
            self.vertexTab[edge[0]][edge[1]] = 1
            # self.vertexTab[edge[1]][edge[0]] = 1
        line = file.readline()
        numberOfPoints = int(line)
        for i in range(numberOfPoints):
            line = file.readline()
            newpoint = line.split(" ")
            newpoint[0] = float(newpoint[0])
            newpoint[1] = float(newpoint[1])
            newpoint = Point(newpoint[0], newpoint[1])
            self.pointsTab.append(newpoint)
        file.close()

    def importfromFileProblemTwo(self,filename):
        file = open(filename, 'r')
        while True:
            line = file.readline()
            if(len(line) == 0):
                break
            self.melodyTab.append(line)

    def importfromFileProblemThree(self,filename):
        file = open(filename, 'r')
        line = file.readline()
        numberofguards = int(line)
        for i in range(numberofguards):
            line = file.readline()
            self.guardsTab.append(int(line))





if __name__ == "__main__":
    filename = input("podaj nazwe pliku: ")
    fromfile = FromFile()
    fromfile.importfromFileProblemOne(filename)
    # fromfile.printVertexTab()
    print(fromfile.pointsTab)