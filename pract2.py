import GUI
import HAL
import utm
# Enter sequential code!

boat_lat = 40 + 16/60 + 48.2/3600 
boat_long = 3 + 49/60 + 03.5/3600

victim_lat = 40 + 16/60 + 47.23/3600
victim_long = 3 + 49/60 + 01.78/3600

coords_utm_boat = utm.from_latlon(boat_lat, boat_long)
coords_utm_victim = utm.from_latlon(victim_lat, victim_long)

dist_x = coords_utm_victim[0] - coords_utm_boat[0]
dist_y = coords_utm_victim[1] - coords_utm_boat[1]

height = 3
HAL.takeoff(height)

while True:
    #act_position = HAL.get_position() #devuelve array [x,y,z]

    #if (act_position[0] < dist_x)


