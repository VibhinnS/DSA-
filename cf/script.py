from typing import Union, Any
class SumError(Exception):
    """return error when type error encountered"""
    
class BoolError(Exception):
    """return error when falsy value detected"""





def sum_func(seq: list | tuple, start: int | float = 0) -> int | float:
    """returns the sum of a sequence or tuple of numbers, optional start param"""
    
    if not isinstance(start, (int, float)):
        raise SumError(f"Start value must be an int or float, not {type(start)}")
    
    total: int = 0
    for element in seq:
        try:
            total += element
        except TypeError as exc:
            raise SumError(f"Error: {exc}")
    return total + start



# print(sum_func([1,2,3,"3"]))




def all_func(seq: Any) -> bool:
    """returns True if all elements in the sequence are truthy, else False"""
    falsy_elements:list[Any] = [0, 0.0, "", False, None]
    try:
        iter(seq)
        for element in seq:
            if element in falsy_elements:
                return False
    except TypeError:
        raise BoolError(TypeError)
    return True


print(all_func(0))



def my_map(func, iterable):
    if not callable(func):
        raise TypeError(f"{func} is not callable")
    
    if not hasattr(iterable, "__iter__"):
        raise TypeError(f"{iterable} is not iterable")



