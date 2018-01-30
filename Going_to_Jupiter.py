# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 20:06:06 2018

@author: mwood
"""
""" 
Going to Jupiter with Python
"""


import matplotlib.pyplot as plt
from orbital import KeplerianElements, earth, Maneuver,plot
from scipy.constants import kilo

orbit_one = KeplerianElements.with_period(90*60,body=earth)
plot(orbit_one)



