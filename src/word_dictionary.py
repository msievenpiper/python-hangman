import random


class WordDictionary:
    words = {
        3: ['two', 'can', 'for', 'the'],
        4: ['four', 'tree', 'lean', 'trim'],
        5: ['happy', 'truth', 'teeth', 'route'],
        6: ['around', 'desert', 'launch', 'square'],
        7: ['account', 'capital', 'drawing', 'keeping'],
        8: ['absolute', 'computer', 'constant', 'database'],
        9: ['aardvarks', 'eagerness', 'habitable', 'sabotaged']
    }

    def fetch_word(self, len):
        """Return a word of a specified length"""
        if not self.validate_length(int(len)):
            return False
        return random.choice(self.words[int(len)])

    def validate_length(self, len):
        """Validate an specified length has a value"""
        return len in self.words.keys()

    def get_options(self):
        """Return the available options for the word length"""
        return self.words.keys()

    def get_options_as_string(self):
        """Get all the options in a concatenated readable string"""
        options = self.get_options()
        string = ''
        for option in options:
            string = string + str(option) + ', '
        return string[:-2]
