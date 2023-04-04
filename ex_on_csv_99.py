def takes_positive(f):
    def wrapper(*args, **kwargs):
        if not (all(type(x) == int for x in args) and all(type(x) == int for y, x in kwargs.items())):
            raise TypeError
        elif any(x < 0 for x in args) or any(x < 0 for y, x in kwargs):
            raise ValueError
        else:
            return f(*args, **kwargs)
    return wrapper
    
@takes_positive
def positive_sum(*args, **kwargs):
    return sum(args) + sum(kwargs.values())
    
print(positive_sum(10, par1=1, sep=4))