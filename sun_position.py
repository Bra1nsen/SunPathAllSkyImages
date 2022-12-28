from suncalc import get_position, get_times
from datetime import datetime

#UTC
date = datetime.now()
#GERMANY
date_ger =datetime.now(germany)
#DRESDEN 
#POSITION ALL SKY IMAGER
lon = 20
lat = 45
get_position(date, lon, lat)
# {'azimuth': -0.8619668996997687, 'altitude': 0.5586446727994595}

#THETA UND PHI 

#ROTATE IMAGE NORTH SOUTH WEST EAST 

#EQUIDISTANT THETA UND R 
#(PHI;R) = (PHI;THETA)
