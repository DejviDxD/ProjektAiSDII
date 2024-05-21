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
    #plt.show()



    graf = Graf(hull,factory)
    graf.make_graf()

    C = graf.apical_coverage()
    print()
    print(graf.edges)
    for i in graf.edges:
        print(i[0],i[1],i[2])

    #graf.print_graf()
    #print("check")
    #print(C)

    for i in C:
        print()
        print(i)
        print(C[i][0],end=" ")
        print(C[i][1])

    built = {key:False for key in C}

    #print(built)

    through_put = Through_Put(plaszczaki)
    przepustowosc = through_put.count_through_put()
    print(przepustowosc)

    for point in C:
        if built[point] == False:
            print()
            
            


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

    


