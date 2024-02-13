"""
This is the "0-add_integer" module.
The 0-add_integer module supplies one function, add_integer(a, b).
"""
def add_integer(a, b=98):
    """
    Function to add two numbers

    Parameters:
    a and b(both int or float)

    Raises:
    TypeError: If 'a' or 'b' is not an integer or float

    Returns:
    int: The return value. The sum of 'a' and 'b'
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    # typecasting
    a = int(a)
    b = int(b)
    return (a + b)
