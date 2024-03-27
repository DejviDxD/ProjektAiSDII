import sys
sys.path.append("..")

from Geometryczne.CPoint import Point

# def graham_scan(points):
#     p0 = min(points,key= lambda p: (p[1],p[0]))


if __name__ == "__main__":
    points = []
    points.append(Point(0,0));
    points.append(Point(7, 0));
    points.append(Point(1, 4));
    points.append(Point(3, 3));
    points.append(Point(3, 1));
    points.append(Point(5, 2));
    points.append(Point(5, 5));
    points.append(Point(9, 6));
    for i in range(len(points)):
        print(points[i].x, points[i].y)
    graham_scan(points)
