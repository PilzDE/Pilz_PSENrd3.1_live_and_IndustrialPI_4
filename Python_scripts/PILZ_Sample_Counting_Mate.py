# (c) 2026 Pilz GmbH & Co. KG
# License CC0-1.0txt 

import paho.mqtt.client as mqtt
import json
import csv
import time
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib.widgets import Button
import matplotlib.image as mpimg

# --------------------------- CONFIGURATION --------------------------- #
# This section defines the detection zones used for target monitoring, the visualization boundaries of the GUI,
# and the positions of the status text elements displayed within the application.
# All values are provided for demonstration purposes and should be adapted to the actual installation setup.
# You will find a picture of this program in the img directory by GitHub. (https://github.com/PilzDE/Pilz_PSENrd3.1_live_and_RevPi_Connect_4/tree/main/img)

# Example detection zone coordinates [m]
ZONE_1 = {"x_min": 0.8, "x_max": 1.9, "y_min": 1.8, "y_max": 2.6}  # Inner zone (orange)
ZONE_2 = {"x_min": 0.8, "x_max": 1.9, "y_min": 0.82, "y_max": 2.6}  # Outer zone (blue)

# Example GUI limits [m]
# Defines the visible coordinate range of the visualization.
GUI_xmin = 0
GUI_xmax = 2.0
GUI_ymin = 0
GUI_ymax = 2.6

# Example status text positions [m]
# Defines the locations of the displayed status messages.
text1_x = -0.79
text1_y = 2.4
text2_x = 1.25
text2_y = 2.4

# This section contains the MQTT communication settings.
# Replace all example values with the parameters of your application.

# MQTT broker configuration
brokerIp = "localhost"
brokerPort = 8883

# Example sensor IDs
deviceId1 = "XXXXXXXXXXXX"  
deviceId2 = "XXXXXXXXXXXX"

# Path to the TLS certificate used for secure MQTT communication.
ca_certs = "</path/to/certs>/server.crt"  

# MQTT topic used to receive position data from all available PSENradar devices
subscribeTopic = "/PSENrd3/+/positionData"

log_file = "count_events.csv"

# --------------------------- GLOBAL STATE --------------------------- #
detObjects = []
xWerte, yWerte, uidLabels = [], [], []
objCounter = 0
targetDetect = 0  # Tracks current detected targets count

# --------------------------- DATA MODEL --------------------------- #
class DetObject:
    def __init__(self, uid, x, y, timestamp):
        self.uid = uid
        self.x = x
        self.y = y
        self.prev_zone = None
        self.current_zone = None
        self.timestamp = timestamp

# --------------------------- UTILITY FUNCTIONS --------------------------- #
def in_zone(x, y, zone):
    return zone["x_min"] <= x <= zone["x_max"] and zone["y_min"] <= y <= zone["y_max"]

def determine_zone(x, y):
    if in_zone(x, y, ZONE_1):
        return "ZONE_1"
    elif in_zone(x, y, ZONE_2):
        return "ZONE_2"
    return None

def log_event(uid, timestamp, direction):
    with open(log_file, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([uid, timestamp, direction])

# --------------------------- CORE LOGIC --------------------------- #
def update_objects(targets, timestamp, topicID):
    global detObjects, xWerte, yWerte, uidLabels, targetDetect, objCounter
    xWerte.clear(); yWerte.clear(); uidLabels.clear()

    if not targets:  # Handle empty or None targets
        targetDetect = 0
        detObjects.clear()
        return

    

    for t in targets:
        uid, x, y = t["UID"], t["xyz"][0], t["xyz"][1]
        if uid[0] in uidLabels:
            continue
        
        obj = next((o for o in detObjects if o.uid == uid), None)

        if obj:
            obj.prev_zone = obj.current_zone
            obj.x, obj.y = x, y
            obj.current_zone = determine_zone(x, y)
            obj.timestamp = timestamp
        else:
            obj = DetObject(uid, x, y, timestamp)
            obj.current_zone = determine_zone(x, y)
            detObjects.append(obj)

        xWerte.append(x)
        yWerte.append(y)
        uidLabels.append(uid[0])
    targetDetect = len(xWerte)
    detObjects = [o for o in detObjects if o.timestamp + 2 >= timestamp]

def process_counts():
    global objCounter
    for obj in detObjects:
        if obj.prev_zone and obj.current_zone and obj.prev_zone != obj.current_zone:
            print(obj)
            if obj.prev_zone == "ZONE_1" and obj.current_zone == "ZONE_2":
                objCounter += 1
                log_event(obj.uid, obj.timestamp, "ENTER")
            elif obj.prev_zone == "ZONE_2" and obj.current_zone == "ZONE_1":
                objCounter -= 1 if objCounter > 0 else 0
                log_event(obj.uid, obj.timestamp, "EXIT")

# --------------------------- MQTT HANDLER --------------------------- #
class mqtt_radar:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.tls_set(ca_certs=ca_certs)
        self.client.tls_insecure_set(True)
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(brokerIp, brokerPort, 60)
        self.payload_sensor1 = []
        self.payload_sensor2 = []

    def on_connect(self, client, userdata, flags, rc):
        print("Connected with result code", rc)
        self.client.subscribe(subscribeTopic)

    def on_message(self, client, userdata, msg):
        
        payload = json.loads(msg.payload)
        DeviceID = msg.topic.split('/')[2]
        targets = payload.get("targets")
        timestamp = payload["header"]["timestamp"][0]
        if not targets:
            targets = []
            
        if DeviceID == deviceId1:
            self.payload_sensor1 = targets
            
        if DeviceID == deviceId2:
            self.payload_sensor2 = targets

        update_objects(self.payload_sensor1 + self.payload_sensor2, timestamp, DeviceID)
            
        process_counts()

    def start(self):
        self.client.loop_start()

    def stop(self):
        self.client.disconnect()
        self.client.loop_stop()

mqtt_rd = mqtt_radar()
mqtt_rd.start()

# --------------------------- GUI --------------------------- #
fig = plt.figure(clear=True)
ax = fig.add_subplot(1, 1, 1)
plt.get_current_fig_manager().set_window_title('Two-Zone Counter')
ax.set_xlim([GUI_xmin, GUI_xmax]);
ax.set_ylim([GUI_ymin, GUI_ymax]);

ax.set_aspect('equal')
ax.set_box_aspect(1)

ax.grid(True)

#Upload backround image: You can set your image as the background here. Your image must be in the same directory.
#background = mpimg.imread("XX.jpg")

#Show Backround 
#ax.imshow(
#background,
#extent=[GUI_xmin, GUI_xmax, GUI_ymin, GUI_ymax], aspect='auto', alpha=0.8, zorder=0)

ax.grid(True)
zone1_rect = plt.Rectangle((ZONE_1["x_min"], ZONE_1["y_min"]), ZONE_1["x_max"]-ZONE_1["x_min"], ZONE_1["y_max"]-ZONE_1["y_min"], color='orange', alpha=0.5)
zone2_rect = plt.Rectangle((ZONE_2["x_min"], ZONE_2["y_min"]), ZONE_2["x_max"]-ZONE_2["x_min"], ZONE_2["y_max"]-ZONE_2["y_min"], color='blue', alpha=0.3)
ax.add_patch(zone2_rect); ax.add_patch(zone1_rect)

handle_text1 = plt.text(text1_x ,text1_y , "0 target(s) detected", size=25, bbox=dict(boxstyle="round", fc="yellow"))
handle_text2 = plt.text(text2_x, text2_y, "0 target(s) counted", size=25, bbox=dict(boxstyle="round", fc="yellow"))
scat = ax.scatter([], [], edgecolors='gray', facecolors='red', alpha=1, s=60)

label_texts = []

# --------------------------- RESET BUTTON --------------------------- #
def reset_counter(event):
    global objCounter
    objCounter = 0
    handle_text2.set_text(f"{objCounter} target(s) counted")
    fig.canvas.draw_idle()

#Button Position:[left, bottom, width, height]
button_ax = fig.add_axes([0.02, 0.02, 0.12, 0.06])
reset_button = Button(button_ax, 'Reset', color='lightgray', hovercolor='tomato')
reset_button.on_clicked(reset_counter)

# --------------------------- UPDATE GUI --------------------------- #
def update_gui(i):
    handle_text1.set_text(f"{targetDetect} target(s) detected")
    handle_text2.set_text(f"{objCounter} target(s) counted")
    data = np.stack((xWerte, yWerte), axis=1) if xWerte and yWerte else np.empty((0, 2))
    scat.set_offsets(data)

    for txt in label_texts:
        txt.remove()
    label_texts.clear()

    for idx, uid in enumerate(uidLabels):
        txt = ax.text(xWerte[idx], yWerte[idx]+0.1, uid%100, fontsize=10, color='black')
        label_texts.append(txt)

    return scat

ani = animation.FuncAnimation(fig=fig, func=update_gui, interval=100, cache_frame_data=False)
plt.show()

mqtt_rd.stop()
