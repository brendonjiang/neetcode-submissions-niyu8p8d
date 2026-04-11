from abc import ABC, abstractmethod
import copy

class Shape(ABC):
    @abstractmethod
    def clone(self):
        pass

class Square(Shape):
    def __init__(self, length: int):
        self.length = length

    def get_length(self) -> int:
        return self.length

    def clone(self) -> Shape:
        # Write your code here
        cloned = copy.deepcopy(self)
        return cloned

class Rectangle(Shape):
    def __init__(self, width: int, height: int):
        self.width = width
        self.height = height

    def get_width(self) -> int:
        return self.width

    def get_height(self) -> int:
        return self.height

    def clone(self) -> Shape:
        # Write your code here
        cloned = copy.deepcopy(self)
        return cloned

class Test:
    def clone_shapes(self, shapes: List[Shape]) -> List[Shape]:
        # Write your code here
        output = []
        for shape in shapes:
            output.append(shape.clone())

        return output
