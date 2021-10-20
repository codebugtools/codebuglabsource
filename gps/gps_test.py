import cbc
from inventthings import gps
import time

#wait until locked onto satelite
while not gps.gps_sensor.fix_valid:
    cbc.display.scroll_text("waiting")
    time.sleep(5)

#once locked on, scroll lat and lon
lat = gps.deg_decmin_to_dec_deg(gps.gps_sensor.lat)
lon = gps.deg_decmin_to_dec_deg(gps.gps_sensor.lon)
cbc.display.scroll_text("{},{}".format(str(lat), str(lon)))