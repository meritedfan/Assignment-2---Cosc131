import numpy as np
import matplotlib.pyplot as plt

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

def load_raw_data_dict(filename):
    """ takes a csv file and turns it into a dictionary """
    new_dict = {}
    content = np.genfromtxt(filename, delimiter=",", dtype=str)
    keys = content[0]
    content = content[1:, :]
    for i in range(0, len(keys)):
        new_dict[keys[i]] = content[:, i]
    new_dict = {k: v.tolist() for k, v in new_dict.items()}
    return new_dict

def draw_bars_snapshot_tli3(filename):
    """ plots data """
    dictionary = load_raw_data_dict(filename)
    tli3 = raw_data_to_tli3s(dictionary)
    xs = dictionary["lake_name"]
    ys = tli3
    axes = plt.axes()
    axes.bar(xs, ys, tick_label=xs, color="indigo")
    axes.tick_params(axis='x', labelrotation=90)
    axes.set_title(f"Snapshot TLI3s from {filename}")
    axes.set_xlabel("Lake")
    axes.set_ylabel("TLI3")

    plt.tight_layout()
    plt.show()

draw_bars_snapshot_tli3("snapshot_02.csv")
draw_bars_snapshot_tli3("snapshot_01.csv")  

#result = draw_bars_snapshot_tli3("snapshot_02.csv")
#for col_name, data in result.items():
#    print(f"'{col_name}': {data}")