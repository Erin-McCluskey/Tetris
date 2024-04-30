from abc import ABC, abstractmethod

class shapes_abtract(ABC):

    @abstractmethod
    def update_init(self):
        name: str
        colour: tuple
        shape_space: list
