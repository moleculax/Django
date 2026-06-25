#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
@author: moleculax
"""

import pandas as pd # 
import numpy as np
import matplotlib.pyplot as plt
np.random.seed(0)
values = np.random.randn(100) 
s = pd.Series(values) 
s.plot(kind='hist', title='Distribucion de valores aleatorios') 
plt.show()