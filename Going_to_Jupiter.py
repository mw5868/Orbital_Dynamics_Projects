# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 20:06:06 2018

@author: mwood
"""
""" 
Going to Jupiter with Python
"""

import numpy as np
import matplotlib.pyplot as plt
plt.ion()

import astropy.units as u
from astropy.time import Time
from astropy.coordinates import solar_system_ephemeris

from poliastro.bodies import Sun, Earth, Jupiter
from poliastro.twobody import Orbit
from poliastro.maneuver import Maneuver
from poliastro.iod import izzo
from poliastro.plotting import plot, OrbitPlotter
from poliastro.util import norm

solar_system_ephemeris.set("jpl")

