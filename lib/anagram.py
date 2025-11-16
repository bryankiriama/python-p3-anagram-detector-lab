# your code goes here!
class Anagram:
    def __init__(self, word):
        self.word = word.lower()
        self.sorted_word = sorted(self.word)

    def match(self, words):
        return [
            letter for letter in words
            if sorted(letter.lower()) == self.sorted_word and letter.lower() != self.word
        ]