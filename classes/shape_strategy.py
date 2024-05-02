from classes.shapes_abstract import shapes_abtract
from classes.shape import shape

class S_strategy(shapes_abtract, shape):
    def update_init(self):
        self.name = "S"
        self.colour = (0, 255, 0)
        self.shape_space = [
            ['.....',
            '......',
            '..00..',
            '.00...',
            '.....'],

            ['.....',
            '..0..',
            '..00.',
            '...0.',
            '.....']
            ]

class Z_strategy(shapes_abtract, shape):
    def update_init(self):
        self.name = "Z"
        self.colour = (255, 0, 0)
        self.shape_space = [
            ['.....',
            '.....',
            '.00..',
            '..00.',
            '.....'],

            ['.....',
            '..0..',
            '.00..',
            '.0...',
            '.....']
            ]

class I_strategy(shapes_abtract, shape):
    def update_init(self):
        self.name = "I"
        self.colour = (0, 255, 255)
        self.shape_space = [
            ['..0..',
            '..0..',
            '..0..',
            '..0..',
            '.....'],

            ['.....',
            '0000.',
            '.....',
            '.....',
            '.....']
            ]

class O_strategy(shapes_abtract, shape):
    def update_init(self):
        self.name = "O"
        self.colour = (255, 255, 0)
        self.shape_space = [
            ['.....',
            '.....',
            '.00..',
            '.00..',
            '.....']
            ]

class J_strategy(shapes_abtract, shape):
    def update_init(self):
        self.name = "J"
        self.colour = (255, 165, 0)
        self.shape_space = [
            ['.....',
            '.0...',
            '.000.',
            '.....',
            '.....'],
            ['.....',
            '..00.',
            '..0..',
            '..0..',
            '.....'],
            ['.....',
            '.....',
            '.000.',
            '...0.',
            '.....'],
            ['.....',
            '..0..',
            '..0..',
            '.00..',
            '.....']
            ]

class L_strategy(shapes_abtract, shape):
    def update_init(self):
        self.name = "L"
        self.colour = (0, 0, 255)
        self.shape_space = [
            ['.....',
            '...0.',
            '.000.',
            '.....',
            '.....'],

            ['.....',
            '..0..',
            '..0..',
            '..00.',
            '.....'],

            ['.....',
            '.....',
            '.000.',
            '.0...',
            '.....'],

            ['.....',
            '.00..',
            '..0..',
            '..0..',
            '.....']
            ]

class T_strategy(shapes_abtract, shape):
    def update_init(self):
        self.name = "T"
        self.colour = (128, 0, 128)
        self.shape_space = [['.....',
            '..0..',
            '.000.',
            '.....',
            '.....'],

            ['.....',
            '..0..',
            '..00.',
            '..0..',
            '.....'],

            ['.....',
            '.....',
            '.000.',
            '..0..',
            '.....'],

            ['.....',
            '..0..',
            '.00..',
            '..0..',
            '.....']
            ]