
class Point:
    def __init__(self,x,y) -> None:
        self.x,self.y = x,y

    def subtract(self, p):
        return Point(self.x - p.x, self.y - p.y)
    def __str__(self) -> str:
        return str(self.x)+" "+str(self.y)