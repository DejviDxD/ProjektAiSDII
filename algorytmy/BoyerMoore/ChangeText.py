class ChangeText:
    def __init__(self,text,patterns_tab):
        self.text = text
        self.patterns_tab = patterns_tab

    def change(self):
        for index in self.patterns_tab:
                new_text = self.text[:index] + 'b' + self.text[index+1:]
                self.text = new_text