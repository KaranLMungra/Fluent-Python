from vector_2d import Vector


def vector_display(v: Vector):
    # Because the str dunder method is not implemented it fallback to repr dunder method.
    print(f"{v}")
    print(f"  abs = {abs(v)}")
    print(f"  bool = {bool(v)}")


def main() -> None:
    v1 = Vector(3, 4)
    v2 = Vector(5, 12)
    vector_display(v1)
    vector_display(v2)
    print("Vector Addition:")
    v3 = v1 + v2
    vector_display(v3)
    print("Scalar Multiplication:")
    v4 = v3 * 4
    vector_display(v4)
