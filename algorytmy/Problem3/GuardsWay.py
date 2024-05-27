def guardsWay(lanternTab,guards_energy):
    max_distance = 2 + (guards_energy-1)//5
    current_place = 0
    current_place = maks(lanternTab,0,max_distance,15)
    print("zatrzymanie  1  w punkcie ",current_place," który ma jasnosc ",lanternTab[current_place])
    i = 1
    while (current_place <= len(lanternTab) and i < len(lanternTab)) :
        i+=1
        if(current_place+max_distance >= len(lanternTab)):
            break
        else:
            current_place = maks(lanternTab,current_place+1,current_place+max_distance+1,lanternTab[current_place])
        print("zatrzymanie ",i," w punkcie ", current_place, " który ma jasnosc ", lanternTab[current_place])


def maks(tab,start,stop,value):
    result = tab[start]
    index = start
    for i in range(start,stop):
        if(result > value):
            result = tab[i]
            index = i
        if(tab[i] > result and tab[i] <= value):
            result = tab[i]
            index = i
    return index


if __name__ == "__main__":
    lTab = [1,5,6,12,5,7,5,12,1,15]

    guardsWay(lTab,7)