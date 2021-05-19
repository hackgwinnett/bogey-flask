import pandas as pd
from termcolor import colored
def rank_pd(filename):
    final_vals = {}
    my_csv = pd.read_csv(filename)
    column = list(my_csv["Composite Score"])
    column2 = list(my_csv["Project Name"])
    res = {column2[i]: column[i] for i in range(len(column2))}
    print(res)
    final_vals = sorted(res.items(), key = lambda kv:(kv[1], kv[0]))
    final_vals = final_vals[::-1]
    print(final_vals)
    return final_vals










    #print(column)
    #sorted_comps = sorted(column)
    #print(sorted_comps)

    #for val in sorted_comps:
        #print("z")
        #row = my_csv.loc[val]
        #print(colored(row, "green"))
        #print(row)
        #print(row[0])
        #final_vals[row[0]] = val
        
        # final_vals[row[0]].append(val)
    
        


#  print(sorted(key_value.items(), key = 
             # lambda kv:(kv[1], kv[0])))  




