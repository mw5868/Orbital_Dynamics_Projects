from numpy import radians
from scipy.constants import kilo
from orbital import earth, KeplerianElements, plot, earth_sidereal_day, Maneuver,plot3d
# Define the orbital parameters
orbit3 = KeplerianElements.with_altitude(1000*kilo,body=earth, e=0.5)
# Define the maneuver type, and parameters
man7 = Maneuver.hohmann_transfer_to_altitude(10000*kilo)
# Plots in 3d the orbital parameters, including the defined maneuver.
plot3d(orbit3,title='Maneuver',maneuver=man7)
