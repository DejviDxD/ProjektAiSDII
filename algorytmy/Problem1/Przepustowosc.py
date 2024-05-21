import sys
sys.path.append("..")

from EdmundsaKarpa.EK import FF

class Through_Put:
    def __init__(self,plaszczaki) -> None:
        self.plaszczaki = plaszczaki
    
    def count_through_put(self):
        g = FF(self.plaszczaki)
        #print("Maksymalna przepustowosc w sieci wynosi %d " % g.ford_fukelson(0, len(self.plaszczaki)-1))
        return g.ford_fukelson(0,len(self.plaszczaki)-1)