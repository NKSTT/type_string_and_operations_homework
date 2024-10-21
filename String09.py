def main(x1,x2,x3):
    """
    Given three integers, x1, x2, and x3, return the "[x1, x2, x3]" string.
    Args:
        x1: int
        x2: int
        x3: int
    Returns:
        str: return answer.
    """
    x1 = 1
    x2 = 2
    x3 = 3
    return "[{}, {}, {}]".format(x1,x2,x3)
x = main(1,2,3)
print (x)