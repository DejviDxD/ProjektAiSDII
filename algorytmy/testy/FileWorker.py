from algorytmy.Geometryczne.CPoint import Point
class FromFile:

    def __init__(self):
        self.pointsTab = []

    def printPoints(self):
        for i in self.pointsTab:
            print(i.x,i.y)

    def printVertexTab(self):
        for i in self.vertexTab:
            print(i)

    def importformFile(self,filename):
        file = open(filename, 'r')
        line = file.readline()
        numberOfVertex = int(line)
        self.vertexTab = [[0 for _ in range(numberOfVertex)] for _ in range(numberOfVertex)]
        line = file.readline()
        numberOfEdges = int(line)
        for i in range(numberOfEdges):
            line = file.readline()
            edge = line.split(" ")
            edge[0] = int(edge[0])
            edge[1] = int(edge[1])
            self.vertexTab[edge[0] - 1][edge[1] - 1] = 1
            self.vertexTab[edge[1] - 1][edge[0] - 1] = 1
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


if __name__ == "__main__":
    filename = input("podaj nazwe pliku: ")
    fromfile = FromFile()
    fromfile.importformFile(filename)
    # fromfile.printVertexTab()
    print(fromfile.pointsTab)