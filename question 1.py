import numpy as np

def trophic_level_index(chla, tn, tp):
    """ takes a set of numpy arrays and returns
    the TLI3 values for each set of columns """
    
    tlc = 2.22 + 2.54 * np.log10(chla)
    tln = -3.61 + 3.01 * np.log10(tn)
    tlp = 0.218 + 2.92 * np.log10(tp)
    
    average = (tlc[:] + tln[:] + tlp[:]) / 3
    return average