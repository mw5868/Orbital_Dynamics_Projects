# -*- coding: utf-8 -*-
"""
Created on Thu Jan 25 19:47:01 2018

@author: mwood
"""

import numpy as np
import matplotlib.pyplot as plt
plt.ion()

from astropy import units as u

from poliastro.bodies import Earth, Mars, Sun
from poliastro.twobody import Orbit

plt.style.use("seaborn")

r = [-6045,-3490,2500]*u.km
v = [-3.4,6.6,2.5]*u.km/u.s

ss = Orbit.from_vectors(Earth, r, v)
print(ss)

from poliastro.plotting import plot
#plot(ss)

a = 1.523679 * u.AU
ecc = 0.093315 * u.one
inc = 1.85 * u.deg
raan = 49.562 * u.deg
argp = 286.537 * u.deg
nu = 23.33 * u.deg

ss = Orbit.from_classical(Sun, a, ecc,inc,raan,argp,nu)
#plot(ss)

from poliastro.examples import iss
print(iss)


from poliastro.maneuver import Maneuver
dv = [5,0,0]*u.m/u.s
man = Maneuver.impulse(dv)
man = Maneuver((0*u.s,dv))

from astropy import time
epoch = time.Time("2018-01-25 20:00")
from poliastro import ephem
new = Orbit.from_body_ephem(Earth, epoch)
print(new)

