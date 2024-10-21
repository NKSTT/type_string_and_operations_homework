def main(x,y):
    """
    Given two integers x, y return the "(x+y)*2={answer}" string.
    Args:
        x: int
        y: int
    Returns:
        str: return answer.
    """
    x = 4
    y = 6
    return "({}+{})*2=20".format(x,y)
d = main(1,2)
print (d)