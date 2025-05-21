""" program \that does somethign """
import matplotlib.pyplot as plt
import numpy as np
import os.path

def float_array(string_list):
    """ converts a given list of values in string 
    format and returns the list converted into an array """
    return np.array(string_list, dtype=float)

def get_filename():
    """ gets filename """
    while True:
        filename = input("Input filename: ")
        if os.path.isfile(filename):
            return filename
        else:
            print('File cannot be found!')

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

def choose_lakes(info_dict):
    """ gets choosen lake """
    lakes = list(info_dict.keys())
    lakes.pop(0)
    lakes = sorted(lakes)
    while True:
        print("Choose a lake:")
        for lake in lakes:
            print(f"     {lake}")
        lake_name = input("Input lake name: ")
        if lake_name in lakes:
            return lake_name
        else:
            print("Lake name cannot be found!")

def draw_time_series_fitted(filename, lake_name):
    """ plots a time lake graph """
    new_dict = load_raw_data_dict(filename)
    years = float_array(new_dict["year"])
    values = float_array(new_dict[lake_name])
    axes = plt.axes()
    axes.plot(years, values, "bo-", label="actual")
    m, c = np.polyfit(years, values, 1)
    y_fitted = m * years + c
    axes.plot(years, y_fitted, color="green", linestyle="dotted", label="fitted")
    axes.set_title(f"TLI3 over time for {lake_name}")
    axes.set_xlabel("Year")
    axes.set_ylabel("TLI3")
    axes.legend()
    axes.grid(True)
    plt.show()

def main():
    """ main function """
    filename = get_filename()
    content = load_raw_data_dict(filename)
    choosen_lake = choose_lakes(content)
    draw_time_series_fitted(filename, choosen_lake)

main()