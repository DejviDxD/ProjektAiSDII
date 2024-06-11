import math
import random

from Geometryczne.CPoint import Point
from Graham.CGraham_hull import Graham_hull
from testy.FileWorker import FromFile
from BoyerMoore.ChangeText import ChangeText
from BoyerMoore.Boyer_Moore import BoyerMoore
from Huffmann.Huffmann import Huffman,huffman_decoding,huffman_encoding
from Problem1.PokrycieWierzcholkow import Graf
from Problem1.Przepustowosc import Through_Put
from Problem3.GuardsWay import guardsWay

import matplotlib.pyplot as plt
import os

if __name__ == "__main__":
    path = os.path.dirname(os.path.abspath(__file__))


    #Problem 1
    print("Problem 1")
    filename = input("Podaj nazwe testu:")
    file_directory = f"/testy/problem_one/{filename}"

    #Pobieranie danych do problemu 1
    file_worker = FromFile()
    file_worker.importfromFileProblemOne(path + file_directory)

    points = file_worker.pointsTab
    plaszczaki = file_worker.vertexTab

    #Tworzenie otoczki wypukłej wraz z animacją graficzną
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
    plt.title("Wstępne projektowanie muru")
    plt.savefig(f'{directory}/hull_step_final.png')

    #Ustawienie punktu fabryki
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


    #Utworzenie drogi dla plaszczaków
    graf = Graf(hull,factory)
    graf.make_graf()
    C = graf.apical_coverage()


    through_put = Through_Put(plaszczaki)
    przepustowosc = through_put.count_through_put()


    #Tworzenie animacji dla trasy płaszczaków w budowaniu muru wraz z wynikiem pierwszego problemu
    directory = path + '/Graham/Create_wall'
    graham_hull.delete_hull_pictures(directory)

    plt.scatter([p.x for p in points], [p.y for p in points], color="black")
    plt.plot([p.x for p in hull], [p.y for p in hull], color="blue")
    plt.scatter(factory.x, factory.y, color="red")


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
        plt.pause(1)
        j += 1
        time_cost += math.ceil(edge[2] / przepustowosc) * list(C.values())[i][2]
        wall_length += edge[2]
        while(edge[2] > 0):
            edge[2] -= przepustowosc
            stack.append(edge[0])
            stack.append((edge[1]))
            plt.plot([p.x for p in stack], [p.y for p in stack], color="red")
            plt.xlabel('X')
            plt.ylabel('Y')
            plt.title("Tworzenie muru")
            plt.savefig(f'{directory}/create_wall{j}.png')
            plt.pause(1)
        edge[3] = True
        factory_ways.pop()
        plt.plot([p.x for p in stack], [p.y for p in stack], color="green")
        plt.xlabel('X')
        plt.ylabel('Y')
        plt.title("Tworzenie muru")
        plt.savefig(f'{directory}/create_wall{j}.png')
        plt.pause(1)
        j += 1
        stack = []
    
    plt.show()

    print()
    print(f"Czas dostawy: {round(time_cost,2)}")
    print(f"Długość muru: {wall_length}")



    #Problem 2
    print("Problem 2")
    filename = input("Podaj nazwe testu:")

    file_directory = f"/testy/problem_two/{filename}"

    #Pobranie danych do problemu 2
    file_worker.importfromFileProblemTwo(path + file_directory)
    melodyTab = file_worker.melodyTab

    # Wyświetlenie nie naprawionej jeszcze melody
    print("Melodia:")
    for text in melodyTab:
        print(text, end='')
    print()
    print()

    patterns_tab = {}
    print("Standardowo zamieniamy 'poli' na 'boli' ale płaszczak ma możliwość wybrania swojego słowa na zamianę.")
    word = input("Jaki wzorzec chcesz dodatkowo zmienić: ")
    pattern = input("Na jakie słowo: ")
    patterns_tab[word] = pattern
    patterns_tab["poli"] = "boli"

    #Zamiana słów w melodii
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


    #Zakodowanie melodii
    encoded_text_tab = []
    for text in melodyTab:
        encoded_text, codebook = huffman_encoding(text)
        encoded_text_tab.append(encoded_text)
    print()
    print("Zakodowana melodia:\n")
    for text in encoded_text_tab:
        print(text)
    print()


    #Problem 3
    print("Problem 3")
    filename = input("Podaj nazwe testu:")
    file_directory = f"/testy/problem_three/{filename}"

    #Pobranie danych do Problemu 3
    file_worker.importfromFileProblemThree(path + file_directory)
    guardsTab = file_worker.guardsTab

    #Ustalenie grafiku
    lanternTab = []                                     #lista z wartosciami jasnosci pnktów
    guardsdict = {i:0 for i in range(len(guardsTab))}   #słownik ze straznikami
    schedule = []                                       #grafik
    melody_count_tab = []                               #lista z liczba odsłuchań melodii

    #uzupełnanie słownika
    for i in range(len(guardsTab)):
        guardsdict[i] = guardsTab[i]

    #losowanie wartości jasności
    for i in range(len(hull)):
        lanternTab.append(random.randrange(3,15))

    #informacje dla użytkownika
    print("W tym tygodniu jasnosc punktow muru to: ")
    for i in lanternTab:
        print(i,end=" ")
    print(" ")

    #ustalanie grafiku
    for j in range(7):
        current_energy = max(guardsTab)
        for i in guardsdict:
            if(guardsdict[i] == current_energy and i not in schedule):
                schedule.append(i)
                break
        #print("dnia ",j+1," idzie płaszczak z energią równą ",current_energy)
        guardsTab.remove(current_energy)
        melody_count_tab.append(guardsWay(lanternTab, current_energy))

    #wpisanie grafiku
    print("grafik wyglada tak")
    for i in range(7):
        print("dzien " + str(i+1) +" straznik nr "+ str(schedule[i]) +" odsluchań " + str(melody_count_tab[i]))





    


