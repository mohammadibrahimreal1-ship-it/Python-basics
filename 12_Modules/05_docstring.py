#We use doc string to explain about our module to others who'll import/use them (such as github)

def add(a, b):
    """
    Returns the sum of two numbers.

    Parameters:
    a (int): The first number.
    b (int): The second number.

    Returns:
    int: The sum of the two numbers.
    """
    return a + b


#Here's an e.g.
def sum(a,b):
    '''This will sum two numbers'''
    c = a+b
    return c

print(sum(12,45))
print(sum.__doc__)