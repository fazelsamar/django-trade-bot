from decimal import Decimal


def multiply_two_float(float_one: float, float_two: float) -> float:
    """
    float_one * float_two
    """
    return float(Decimal(str(float_one)) * Decimal(str(float_two)))


def division_two_float(float_one: float, float_two: float) -> float:
    """
    float_one / float_two
    """
    return float(Decimal(str(float_one)) / Decimal(str(float_two)))


def subtraction_two_float(float_one: float, float_two: float) -> float:
    """
    float_one - float_two
    """
    return float(Decimal(str(float_one)) - Decimal(str(float_two)))


def sum_two_float(float_one: float, float_two: float) -> float:
    """
    float_one + float_two
    """
    return float(Decimal(str(float_one)) + Decimal(str(float_two)))
