# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 19:53:22 2017

@author: mwood
"""

from orbital import utilities as ut
import matplotlib.pyplot as plt
from scipy.constants import kilo

radius = ut.altitude_from_radius(5000*kilo, body=earth)
print(radius)
