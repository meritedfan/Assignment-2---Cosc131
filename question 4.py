import numpy as np

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

# test code below

result = load_raw_data_dict('simple_data.csv')
for col_name, data in result.items():
    print(f"'{col_name}': {data}")

result = load_raw_data_dict('simple_data_2.csv')
for col_name, data in result.items():
    print(f"'{col_name}': {data}")