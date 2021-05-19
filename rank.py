import pandas as pd
def rank(filename):
    final_vals = {}
    my_csv = pd.read_csv(filename)
    column = my_csv.column_name
    sorted_comps = column.sort()
    sorted_comps.remove("Composite Score")

    for val in sorted_comps:
        row = my_csv.loc[val]
        final_vals[row[0]].append(val)
    return final_vals
        




