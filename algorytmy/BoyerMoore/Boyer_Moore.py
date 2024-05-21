class BoyerMoore:

    def __init__(self,t,p):
        self.pattern = p
        self.text = t
    def preprocess_strong_suffix(self,shift, bpos, m):
        i = m
        j = m + 1
        bpos[i] = j
        while i > 0:
            while j <= m and self.pattern[i - 1] != self.pattern[j - 1]:

                if shift[j] == 0:
                    shift[j] = j - i
                j = bpos[j]
            i -= 1
            j -= 1
            bpos[i] = j

    def preprocess_case2(self,shift, bpos, m):
        j = bpos[0]
        for i in range(m + 1):
            if shift[i] == 0:
                shift[i] = j

            if i == j:
                j = bpos[j]


    def BM(self, pattern_tab):
        s = 0
        m = len(self.pattern)
        n = len(self.text)

        bpos = [0] * (m + 1)
        shift = [0] * (m + 1)
        self.preprocess_strong_suffix(shift, bpos, m)
        self.preprocess_case2(shift, bpos, m)
        pp = 0
        while s <= n - m:
            j = m - 1
            while j >= 0 and self.pattern[j] == self.text[s + j]:
                j -= 1
            if j < 0:
                pattern_tab.append(s)
                pp += s
                s += shift[0]
            else:
                s += shift[j + 1]

if __name__ == "__main__":
    text = "W laboratorium chemik używał polimerów do stworzenia nowej polisyntezatorowej substancji."
    pat = "poli"
    pattern_tab = []
    search = BoyerMoore(text,pat)
    search.BM(pattern_tab)
    print(pattern_tab)
