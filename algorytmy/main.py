import math

from Geometryczne.CPoint import Point
from Graham.CGraham_hull import Graham_hull
from testy.FileWorker import FromFile
from BoyerMoore.ChangeText import ChangeText
from BoyerMoore.Boyer_Moore import BoyerMoore
from Huffmann.Huffmann import Huffman,huffman_decoding,huffman_encoding
from Problem1.PokrycieWierzcholkow import Graf
from Problem1.Przepustowosc import Through_Put

import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))
    filename = input("Podaj nazwe testu:")
    file_directory = f"/testy/problem_one/{filename}"
    file_worker = FromFile()
    file_worker.importfromFileProblemOne(path + file_directory)
    points = file_worker.pointsTab
    plaszczaki = file_worker.vertexTab


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
    plt.pause(0.1)
    plt.scatter(factory.x,factory.y, color="red")
    plt.savefig(f'{directory}/hull_step_final_factory.png')
    plt.show()



    graf = Graf(hull,factory)
    graf.make_graf()

    C = graf.apical_coverage()
    print()
    print(graf.edges)
    for i in graf.edges:
        print(i[0],i[1],i[2],i[3])

    #graf.print_graf()
    #print("check")
    #print(C)

    print("CCC")
    for i in C:
        print()
        print(i)
        print()
        print(C[i][0],end=" ")
        print()
        print(C[i][1],print(C[i][2]))


    through_put = Through_Put(plaszczaki)
    przepustowosc = through_put.count_through_put()
    print(przepustowosc)

    directory = path + '/Graham/Create_wall'
    graham_hull.delete_hull_pictures(directory)

    plt.scatter([p.x for p in points], [p.y for p in points], color="black")
    plt.plot([p.x for p in hull], [p.y for p in hull], color="blue")
    plt.scatter(factory.x, factory.y, color="red")


    i = 0
    j = 0
    time_cost = 0.0
    wall_length = 0
    stack = []
    factory_ways = []
    for edge in graf.edges:
        factory_ways.append(factory)
        factory_ways.append(edge[0])
        plt.plot([p.x for p in factory_ways], [p.y for p in factory_ways], color="orange")
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title("Tworzenie muru")
        plt.savefig(f'{directory}/create_wall{j}.png')
        plt.pause(0.5)
        j += 1
        time_cost += math.ceil(edge[2] / przepustowosc) * list(C.values())[i][2]
        wall_length += edge[2]
        i += 1
        while(edge[2] > 0):
            edge[2] -= przepustowosc
            stack.append(edge[0])
            stack.append((edge[1]))
            plt.plot([p.x for p in stack], [p.y for p in stack], color="red")
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title("Tworzenie muru")
            plt.savefig(f'{directory}/create_wall{j}.png')
            plt.pause(0.5)
        edge[3] = True
        factory_ways.pop()
        plt.plot([p.x for p in stack], [p.y for p in stack], color="green")
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title("Tworzenie muru")
        plt.savefig(f'{directory}/create_wall{j}.png')
        plt.pause(0.5)
        j += 1
        stack = []
    for i in graf.edges:
        print(i[0],i[1],i[2],i[3])
    
    plt.show()

    print()

    print(f"Czas dostawy: {round(time_cost,2)}")
    print(f"Długość muru: {wall_length}")


    # graf.print_graf()



    filename = input("Podaj nazwe testu:")

    file_directory = f"/testy/problem_two/{filename}"
    file_worker.importfromFileProblemTwo(path + file_directory)
    melodyTab = file_worker.melodyTab

    patterns_tab = {}
    word = input("Jaki wzorzec chcesz dodatkowo zmienić:")
    pattern = input("Na jakie słowo:")
    patterns_tab[word] = pattern
    patterns_tab["poli"] = "boli"

    for word,pattern in patterns_tab.items():
        for i in range(0,len(melodyTab)):
            pattern_tab = []
            melody = BoyerMoore(melodyTab[i],word)
            melody.BM(pattern_tab)
            changeText = ChangeText(melodyTab[i],pattern_tab,pattern,word)
            changeText.change()
            melodyTab[i] = changeText.text
    print("Naprawiona melodia:\n")
    for text in melodyTab:
        print(text,end='')
    print()

    encoded_text_tab = []
    for text in melodyTab:
        encoded_text, codebook = huffman_encoding(text)
        encoded_text_tab.append(encoded_text)
    print()
    print("Zakodowana melodia:\n")
    for text in encoded_text_tab:
        print(text)
    print()

    


