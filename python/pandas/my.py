import json
import pandas as np
from pandas import Series,DataFrame
import matplotlib.pyplot as plt
with open("foods-2011-10-03.json") as data:
    db = json.load(data)
# foods = DataFrame(db)
# print(db[0].keys())
info_keys = ["description","group","id","manufacturer"]
info = DataFrame(db,columns=info_keys)
fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
fig.show()
