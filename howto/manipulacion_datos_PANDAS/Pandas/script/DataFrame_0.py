#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Jun 24 18:42:08 2026
@author: moleculax
"""

import pandas as pd

nombre =  ['PEPE', 'LUPE', 'COQUI']
edades = [28, 34, 29]
paises = ['COLOMBIA', 'ECUADOR', 'URUGUAY']


data = {
        'Nombre':nombre,
        'Edad': edades,
        'Pais': paises
        }

df = pd.DataFrame(data)
print(df)