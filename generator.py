from essential_generators import DocumentGenerator



class WordGenerator:
    def __init__(self):
        self.gen = DocumentGenerator()
        
    def next_sentence(self):
        return self.gen.sentence()
        
    def nect_word(self):
        return self.gen.word()
        
