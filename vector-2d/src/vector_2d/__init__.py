from math import floor, hypot


class Vector:
    def __init__(self, x: int, y: int) -> None:
        self.x = x
        self.y = y
        pass

    def __repr__(self) -> str:
        return f"Vector({self.x}, {self.y})"

    def __abs__(self) -> int:
        return floor(hypot(self.x, self.y))

    def __bool__(self) -> bool:
        return not (self.x and self.y)

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Vector(x, y)

    def __mul__(self, scalar: int):
        x = self.x * scalar
        y = self.y * scalar
        return Vector(x, y)
