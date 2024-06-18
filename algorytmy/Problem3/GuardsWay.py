def guardsWay(lanternTab,guards_energy): #ustalanie przejscia straznika
    max_distance = 2 + (guards_energy-1)//5
    melody_count = 0
    current_place = 0
    lace_before = current_place
    if __name__ == "__main__":
        print("dystans: "+str(max_distance))
    current_place = maks(lanternTab, 0, max_distance, 16)
    if __name__ == "__main__":
        print("zatrzymanie  1  w punkcie ",current_place," który ma jasnosc ",lanternTab[current_place])
    i = 1
    while (current_place+1 < len(lanternTab) and i < len(lanternTab)) :
        i+=1
        place_before = current_place
        current_place = maks(lanternTab, place_before + 1, place_before + max_distance + 1, lanternTab[place_before])
        if(current_place == -1):
            return melody_count
        if(lanternTab[current_place] >= lanternTab[place_before]):
            if __name__ == "__main__":
                print("zatrzymanie ", i, " w punkcie ", current_place, " który ma jasnosc ", lanternTab[current_place]," przerwa na sluchanie muzyki")
            melody_count += 1
        else:
            if __name__ == "__main__":
                print("zatrzymanie ", i, " w punkcie ", current_place, " który ma jasnosc ", lanternTab[current_place])
    return melody_count


def maks(tab,start,stop,value):                 #liczenie maksa
    result = tab[start]
    index = start
    for i in range(start,stop):
        if(i >= len(tab)):                      #zatrzymywanie po przejsciu tablicy
            break
        if(result >= value and tab[i] < value): #korekta wartosci poczatkowej
            result = tab[i]
            index = i
        if(tab[i] >= result and tab[i] < value):    #znajdowanie pojelnego maksa
            result = tab[i]
            index = i
    if(value == 16):
        return index
    if(tab[index] > value):
        if(stop >= len(tab)):
            return -1
        return maks(tab,start,stop,16)
    return index


if __name__ == "__main__":
    lTab = [1,3,12,3,13,10,6,5,5,12]
    lTab2 = [2, 14, 4, 5, 13, 1, 14]

    guardsWay(lTab,6)