class GameRender:
    state: 0

    printables = {
        6: '''
          +---+
          |   |
              |
              |
              |
              |
        =========
        ''',
        5: '''
          +---+
          |   |
          O   |
              |
              |
              |
        =========
        ''',
        4: '''
         +---+
         |   |
         O   |
         |   |
             |
             |
       =========
       ''',
        3: '''
          +---+
          |   |
          O   |
         /|   |
              |
              |
        =========
        ''',
        2: '''
          +---+
          |   |
          O   |
         /|\  |
              |
              |
        =========''',
        1: '''
          +---+
          |   |
          O   |
         /|\  |
         /    |
              |
        =========
        ''',
        0: '''
          +---+
          |   |
          O   |
         /|\  |
         / \  |
              |
        =========
        '''
    }

    def __init__(self, state=0):
        self.state = state

    def render(self):
        print(self.printables[int(self.state)])

    def update_state(self, state=0):
        self.state = state
