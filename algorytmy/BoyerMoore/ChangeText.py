class ChangeText:
    def __init__(self,text,patterns_tab, pattern,word):
        self.text = text
        self.patterns_tab = patterns_tab
        self.pattern = pattern
        self.word = word

    def change(self):
        for index in self.patterns_tab:
            if len(self.word) > len(self.pattern):
                new_text = self.text[:index] + self.pattern + self.text[len(self.word)+index:]
                self.text = new_text
            elif len(self.word) < len(self.pattern):
                length = len(self.pattern) - len(self.word)
                new_text = self.text[:index] + self.pattern + self.text[len(self.pattern) + index - length:]
                self.text = new_text
            else:
                new_text = self.text[:index] + self.pattern + self.text[len(self.pattern) + index:]
                self.text = new_text