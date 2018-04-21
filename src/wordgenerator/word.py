class Word:
    def __init__(self, word):
        self.word = word
        self.characters = list(word)

    def is_letter_in_word(self, letter):
        for l in self.characters:
            if l == letter:
                return True
        return False
