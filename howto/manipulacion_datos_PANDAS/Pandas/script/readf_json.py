#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:00:23 2026

@author: moleculax
"""

import pandas as pd

# Si el JSON está en un archivo
df = pd.read_json('datos.json')
print(df)