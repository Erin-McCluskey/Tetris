class shape():

    def __init__(self):
        self.x = 5
        self.y = 0
        self.rotation = 0

    def get_shape(self, shape_strategy):
       shape_strategy.update_init()
       return shape_strategy