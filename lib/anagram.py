# your code goes here!
# class -> Anagram, instance method -> match()
# when given a word, it checks an array of words and returns it's anagram (a word that has the same letters as the word)
# if there is none, it should return []

class Anagram():
    def __init__(self, word):
        self.word = word
        
    def match(self, words_array):
        return [word for word in words_array if sorted(word) == sorted(self.word)]

# examples    
listen = Anagram("listen")
print(listen.match(['enlists', 'google', 'inlets', 'banana'])) # should return ['inlets]

word = Anagram("word")
print(word.match(['hello', 'goodbye'])) # should return []