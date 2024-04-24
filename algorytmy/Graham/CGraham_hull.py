import functools
import sys
import os
sys.path.append("..")
import matplotlib.pyplot as plt

from Geometryczne.CPoint import Point



class Graham_hull:
    def __init__(self, points):
        self.points = points
    def delete_hull_pictures(self,directory):
        for filename in os.listdir(directory):
            if filename.startswith('hull_'):
                os.remove(os.path.join(directory,filename))


    def cross_product(self,p1: Point,p2: Point):
        return p1.x * p2.y - p2.x * p1.y

    def direction(self,p1: Point,p2: Point,p3: Point):
        return self.cross_product(p3.subtract(p1), p2.subtract(p1))

    def collinear(self, p1: Point,p2: Point,p3: Point):
        return self.direction(p1, p2, p3) == 0

    def distance_sq(self, p1: Point,p2: Point):
        return (p2.x - p1.x) ** 2 + (p2.y - p1.y) ** 2

    def find_min_y(self):
        min_y = 99999999
        min_i = 0
        for i , point in enumerate(self.points):
            if point.y < min_y:
                min_y = point.y
                min_i = i
            if point.y == min_y:
                if(point.x < self.points[min_i].x):
                    min_i = i
        return self.points[min_i], min_i

    def polar_comparator(self,p1,p2,p0):
        d = self.direction(p0,p1,p2)
        if d < 0:
            return -1
        if d > 0:
            return 1
        if d == 0:
            if self.distance_sq(p1,p0) < self.distance_sq(p2,p0):
                return -1
            else:
                return 1


    def graham_scan(self,directory):
        p0, index = self.find_min_y()

        self.points[0],self.points[index] = self.points[index],self.points[0]

        sorted_polar = sorted(self.points[1:], key=functools.cmp_to_key( lambda p1,p2: self.polar_comparator(p1,p2,p0)))

        to_remove = []
        for i in range(len(sorted_polar) - 1):
            d = self.direction(sorted_polar[i],sorted_polar[i + 1], p0)
            if d == 0:
                to_remove.append(i)
        sorted_polar = [i for j, i in enumerate(sorted_polar) if j not in to_remove]

        m = len(sorted_polar)
        if m < 2:
            print("Otoczka wypukła jest pusta")
        else:
            stack = []
            stack.append(self.points[0])
            stack.append(sorted_polar[0])
            stack.append(sorted_polar[1])
            stack_size = 3
            j = 0
            for i in range(2,m):
                while(True):
                    d = self.direction(stack[stack_size - 2], stack[stack_size - 1],sorted_polar[i])
                    if d < 0:
                        break;
                    else:
                        stack.pop()
                        self.plot_hull(stack,self.points[i])
                        j += 1
                        plt.savefig(f'{directory}/hull_step{j}.png')
                        stack_size -= 1
                stack.append(sorted_polar[i])
                self.plot_hull(stack,self.points[i])
                j += 1
                plt.savefig(f'{directory}/hull_step{j}.png')
                stack_size += 1
            return stack


    def plot_hull(self,hull,point):
        plt.clf()
        plt.scatter([p.x for p in self.points], [p.y for p in self.points], color="blue")
        hull_points = hull.copy()
        hull_points.append(point)
        hull_points.append(hull[0])
        plt.plot([p.x for p in hull], [p.y for p in hull], color="red")
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title("Otoczka wypukła")
        plt.pause(0.5)


if __name__ == "__main__":

    points = []
    points.append(Point(0,0))
    points.append(Point(7, 0))
    points.append(Point(1, 4))
    points.append(Point(3, 3))
    points.append(Point(3, 1))
    points.append(Point(5, 2))
    points.append(Point(5, 5))
    points.append(Point(9, 6))
    graham_hull = Graham_hull(points)
    directory = 'Hull_pictures/'
    graham_hull.delete_hull_pictures(directory)
    plt.scatter([p.x for p in points], [p.y for p in points], color="blue")
    plt.savefig(f'Hull_pictures/hull_start.png')
    hull = graham_hull.graham_scan(directory)
    print("Punkty otoczki wypukłej")
    for point in hull:
        print(f"{point.y} , {point.x}")

    hull.append(hull[0])
    plt.plot([p.x for p in hull], [p.y for p in hull], color="red")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Otoczka wypukła")
    plt.savefig(f'Hull_pictures/hull_step_final.png')
    plt.show()
