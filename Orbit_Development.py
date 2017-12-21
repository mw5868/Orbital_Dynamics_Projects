# -*- coding: utf-8 -*-
"""
Created on Thu Dec 21 19:53:22 2017

@author: mwood
"""

from orbital import KeplerianElements, earth,plot,plot3d
import matplotlib.pyplot as plt
from scipy.constants import kilo

flight = KeplerianElements.with_altitude(5000*kilo, body = earth)
plot(flight)
plt.show()
plot3d(flight)
plt.show()
