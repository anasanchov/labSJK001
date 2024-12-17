import GUI
import HAL
import utm
import cv2
import time
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


def move_to_location(target_x, target_y, current_height):
    while not((target_x-1 < HAL.get_position()[0] < target_x+1) and 
              (target_y-1 < HAL.get_position()[1] < target_y+1)):

        GUI.showImage(HAL.get_frontal_image())
        GUI.showLeftImage(HAL.get_ventral_image())

        HAL.set_cmd_pos(target_x, target_y, current_height, angle)
        x_pos = HAL.get_position()[0]
        y_pos = HAL.get_position()[1]
        #print(x_pos)
        #print(y_pos)


 
def detect_victims(image):
    face_cascade = cv2.CascadeClassifier(cv2.data.haarcascades + 'haarcascade_frontalface_default.xml')
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    faces = face_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=5, minSize=(30, 30))
    return faces


def rescure_victims():
    HAL.takeoff(height)

    move_to_location(dist_x, dist_y, height)

    total_victims = 6
    rescued_victims = 0

    while rescued_victims < total_victims:
        front_image = HAL.get_frontal_image()
        left_image = HAL.get_ventral_image()
        
        GUI.showImage(front_image)
        GUI.showLeftImage(left_image)

        victims = detect_victims(front_image)

        #for(x, y, w, h) in 
        print(victims)

        for(x, y, w, h) in victims:
            cv2.rectangle(front_image,(x,y), (x+w, y+h), (0, 255, 0), 2)
            rescued_victims += 1
        
        GUI.showImage(front_image)

        time.sleep(1)
    
    move_to_location(0, 0, height)

    HAL.land()


rescure_victims()


while True:
    pass
    #GUI.showImage(HAL.get_frontal_image())
    #GUI.showLeftImage(HAL.get_ventral_image())





#1. Ir hasta zona de rescate 
#2. Rescatar a los naufragos:
#    - Load * xml              |
#    - Movemos drone           |       cv2
#    - Monitorizar imagen      |
#    - nsq classifier          |

#    - 5 víctimas --> loop

#3. Volver al barco '''
