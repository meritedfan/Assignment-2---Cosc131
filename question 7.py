import matplotlib.pyplot as plt
import numpy as np

def float_array(string_list):
    """ converts a given list of values in string 
    format and returns the list converted into an array """
    return np.array(string_list, dtype=float)

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

def draw_time_series_single(filename, lake_name):
    """ plots a time lake graph """
    new_dict = load_raw_data_dict(filename)
    years = float_array(new_dict["year"])
    values = float_array(new_dict[lake_name])
    axes = plt.axes()
    axes.plot(years, values)
    axes.set_title(f"TLI3 over time for {lake_name}")
    axes.set_xlabel("Year")
    axes.set_ylabel("TLI3")
    axes.grid(True)
    plt.show()

draw_time_series_single("time_series_01.csv","lake2")