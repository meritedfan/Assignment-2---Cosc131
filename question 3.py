import numpy as np

def trophic_level_index(chla, tn, tp):
    """ takes a set of numpy arrays and returns
    the TLI3 values for each set of columns """
    
    tlc = 2.22 + 2.54 * np.log10(chla)
    tln = -3.61 + 3.01 * np.log10(tn)
    tlp = 0.218 + 2.92 * np.log10(tp)
    
    average = (tlc[:] + tln[:] + tlp[:]) / 3
    return average

def float_array(string_list):
    """ converts a given list of values in string 
    format and returns the list converted into an array """
    return np.array(string_list, dtype=float)

def raw_data_to_tli3s(raw_data_dict):
    """ takes a dictionary and returns the TLI3 values
    of the diction keys """
    chla = float_array(raw_data_dict["chla"])
    tn = float_array(raw_data_dict["tn"])
    tp = float_array(raw_data_dict["tp"])

    return trophic_level_index(chla, tn, tp)

# testing code below
raw_data = {
    'lake_id': ['111', '222', '333'],
    'lake_name': ['Lake1', 'Lake2', 'Lake3'], 
    'lake_region': ['north', 'north', 'south'],
    'chla': ['3', '4', '6'],
    'tn': ['1', '2', '4'],
    'tp': ['2', '3', '5']
}
result = raw_data_to_tli3s(raw_data)
print(result)