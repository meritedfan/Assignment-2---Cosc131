import numpy as np

def float_array(string_list):
    """ converts a given list of values in string 
    format and returns the list converted into an array """
    return np.array(string_list, dtype=float)


stringy_floats = ['2.5', '3.25', '0.25']
arr = float_array(stringy_floats)
print(arr)
print(type(arr))

raw = ['2', '3.5', '0.25', '100', '200.125']
arr = float_array(raw)
print(arr)
print(type(arr))