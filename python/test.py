# -*- coding:utf-8 -*-
from collections import namedtuple
from copy import copy,deepcopy
import pandas as pd
import numpy as np

d = pd.DataFrame(np.arange(12).reshape(3,4),columns=['a','b','c','d'])
print(d)
d.drop(0)
print(d)
a = dict()
a.keys()