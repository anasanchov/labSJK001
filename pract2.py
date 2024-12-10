import GUI
import HAL
import utm
import cv2
# Enter sequential code!

boat_lat = 40 + 16/60 + 48.2/3600 
boat_long = 3 + 49/60 + 03.5/3600

victim_lat = 40 + 16/60 + 47.23/3600
victim_long = 3 + 49/60 + 01.78/3600

coords_utm_boat = utm.from_latlon(boat_lat, boat_long)
coords_utm_victim = utm.from_latlon(victim_lat, victim_long)

dist_y = coords_utm_victim[0] - coords_utm_boat[0]
dist_x = coords_utm_boat[1] - coords_utm_victim[1] 
height = 3
HAL.takeoff(height)
angle = 0.6

x_pos = HAL.get_position()[0]
y_pos = HAL.get_position()[1]

print("DISTANCIA X: ", dist_x)
print("DISTANCIA Y: ",dist_y)

    #act_pos = HAL.get_position() # sacar la posición hasta que esté en el rango  dentro de las x

while dist_x != x_pos and dist_y != y_pos: #ajustar valores, no redondeados (poner un rango, pe estar entre dist_y -1 y dist_y +1 o así)
    #x_pos, y_pos = HAL.get_position() #devuelve array [x,y,z]
    #print(HAL.get_position())
    #print(y_pos)
    HAL.set_cmd_pos(dist_x, dist_y, height, angle)
    x_pos = HAL.get_position()[0]
    y_pos = HAL.get_position()[1]
    print(x_pos)
    print(y_pos)

    #if (act_position[0] < dist_x)

    GUI.showImage(HAL.get_frontal_image())
    GUI.showLeftImage(HAL.get_ventral_image())


while True:
    #GUI.showImage(HAL.get_frontal_image())
    #GUI.showLeftImage(HAL.get_ventral_image())


face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')

 
#1. Ir hasta zona de rescate
#2. Rescatar a los naufragos:
#    - Load * xml              |
#    - Movemos drone           |       cv2
#    - Monitorizar imagen      |
#    - nsq classifier          |

#    - 5 víctimas --> loop

#3. Volver al barco '''


