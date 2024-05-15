from Geometryczne.CPoint import Point
from Graham.CGraham_hull import Graham_hull
from testy.FileWorker import FromFile

import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = input("Podaj nazwe testu: ")
    file_directory = f"/testy/{filename}"
    print(file_directory)
    file_worker = FromFile()
    file_worker.importformFile(path + file_directory)
    points = file_worker.pointsTab
    # points.append(Point(0,0))
    # points.append(Point(7, 0))
    # points.append(Point(1, 4))
    # points.append(Point(3, 3))
    # points.append(Point(3, 1))
    # points.append(Point(5, 2))
    # points.append(Point(5, 5))
    # points.append(Point(9, 6))
    graham_hull = Graham_hull(points)
    directory = path + '/Graham/Hull_pictures'
    graham_hull.delete_hull_pictures(directory)
    plt.scatter([p.x for p in points], [p.y for p in points], color="black")
    plt.savefig(f'{directory}/hull_start.png')
    hull = graham_hull.graham_scan(directory)
    print("Punkty otoczki wypukłej")
    for point in hull:
        print(f"{point.y} , {point.x}")

    hull.append(hull[0])
    plt.plot([p.x for p in hull], [p.y for p in hull], color="blue")
    plt.xlabel('X')
    plt.ylabel('Y')
    plt.title("Otoczka wypukła")
    plt.savefig(f'{directory}/hull_step_final.png')
    factory = points[0]
    if(factory in hull):
        for i in range(1,len(points)):
            if points[i] not in hull:
                factory = points[i]
                break
    plt.scatter(factory.x,factory.y, color="red")
    plt.savefig(f'{directory}/hull_step_final_factory.png')
    plt.show()
