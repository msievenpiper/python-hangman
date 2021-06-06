from word_dictionary import WordDictionary
from game_renderer import GameRender


class Game:
    completed = False

    guesses = []

    correct = []

    incorrect = []

    selected_word = ''

    dictionary = None

    renderer = None

    lives = 6

    def __init__(self):
        self.dictionary = WordDictionary()
        self.renderer = GameRender()

    def start(self):
        self.reset()
        self.renderer.update_state()
        self.renderer.render()
        print('Select a word length from the available options: ' + self.dictionary.get_options_as_string())
        difficulty = input('Write selection here: ')
        self.selected_word = self.dictionary.fetch_word(difficulty)
        self.renderer.update_state(self.lives)
        self.renderer.render()

    def reset(self):
        self.completed = False
        self.guesses = []
        self.correct = []
        self.incorrect = []
        self.selected_word = ''
        self.lives = 6

    def guess(self):
        guess = input('Your guess letter: ')

        if len(guess) == len(self.selected_word) and self.selected_word == guess:
            self.finish()

        if len(guess) == 0:
            print('You have to guess a single letter')
            return

        if len(guess) > 1:
            print('It can only be a single letter')
            return

        if guess in self.guesses:
            print('You cannot guess the same letter again')
            return

        self.guesses.append(guess)
        if guess in self.selected_word:
            self.correct.append(guess)
        else:
            self.incorrect.append(guess)
            self.lives = self.lives - 1

        print('You have ' + str(self.lives) + ' lives remaining')
        self.renderer.update_state(self.lives)
        self.renderer.render()
        self.print_current_guesses()
        self.print_correct_places()

        if self.lives <= 0:
            self.finish('Loss')

        if self.check_if_word_is_correctly_guessed():
            self.finish('Win')

    def check_if_word_is_correctly_guessed(self):
        return self.correct == list(dict.fromkeys(list(self.selected_word)))

    def print_correct_places(self):
        string = ''
        for letter in self.selected_word:
            if letter in self.correct:
                string = string + letter
            else:
                string = string + '_'
        print(string)

    def finish(self, option='Win'):
        self.completed = True
        if option == 'Win':
            print('You guessed correctly: ' + self.selected_word)
            print('Thank you for playing')
        else:
            print('You failed to guess: ' + self.selected_word)
            print('You were Hanged!!!')
        exit()

    def print_current_guesses(self):
        string = 'You have currently guessed: '
        for guess in self.guesses:
            string = string + str(guess) + ', '
        string = string[:-2]
        print(string)
