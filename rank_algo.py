import pandas as pd
def rank_pd(filename):
    final_vals = {}
    my_csv = pd.read_csv(filename)
    column = list(my_csv["Composite Score"])
    column2 = list(my_csv["Project Name"])
    res = {column2[i]: column[i] for i in range(len(column2))}
    final_vals = sorted(res.items(), key = lambda kv:(kv[1], kv[0]))[::-1]
    return final_vals
