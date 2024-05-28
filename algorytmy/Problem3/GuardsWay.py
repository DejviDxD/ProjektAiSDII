def guardsWay(lanternTab,guards_energy):
    max_distance = 2 + (guards_energy-1)//5
    print(max_distance," dystans")
    current_place = 0
    lace_before = current_place
    current_place = maks(lanternTab, 0, max_distance, 15)
    print("zatrzymanie  1  w punkcie ",current_place," który ma jasnosc ",lanternTab[current_place])
    i = 1
    while (current_place+1 < len(lanternTab) and i < len(lanternTab)) :
        i+=1
        place_before = current_place
        current_place = maks(lanternTab, place_before + 1, place_before + max_distance + 1, lanternTab[place_before])
        if(lanternTab[current_place] > lanternTab[place_before]):
            print("zatrzymanie ", i, " w punkcie ", current_place, " który ma jasnosc ", lanternTab[current_place]," przerwa na sluchanie muzyki")
        else:
            print("zatrzymanie ",i," w punkcie ", current_place, " który ma jasnosc ", lanternTab[current_place])


def maks(tab,start,stop,value):
    result = tab[start]
    index = start
    #print(value,"= VAL")
    for i in range(start,stop):
        #print("\n",i)
        #print("res =",result)
        if(i >= len(tab)):
            break
        if(result > value and tab[i] < value):
            result = tab[i]
            index = i
        if(tab[i] > result and tab[i] <= value):
            result = tab[i]
            index = i
            #print(result,"3")
    #print(index)
    if(tab[index] > value):
        #print(tab[index], "> ", value)
        return maks(tab,start,stop,15)
    return index


if __name__ == "__main__":
    lTab = [2,2,1,15,7,5,12,6,11]
    lTab2 = [15,6,8,6,5,7,4,3]

    guardsWay(lTab,6)