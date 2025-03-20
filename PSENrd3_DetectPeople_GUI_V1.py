import paho.mqtt.client as mqtt
import json
import tkinter
import threading
import time

# --------------------------- variables for mqtt communication --------------------------------#
# ------- for PSENradar and mqtt-broker modify(customize)
brokerIp = "localhost"  # ip address of the mqtt-broker (for example "192.168.0.102"), if broker is installed locally, set to "localhost"
brokerPort = 8883  # port number of the mqtt-broker
deviceId = "XXXXXXXXXXXX"  # sensor mac-address
ca_certs = "/XXX/XXX/XXX/XXX"  # path for the certificates
# --------------------------------
subscribeTopic = f"/PSENrd3/{deviceId}/positionData"  # mqtt subscribe topic

# ---------------------------------- variables for gui -------------------------------------#
root = tkinter.Tk()
root.title("People Counter")
root.geometry("500x150")
textVar1 = tkinter.StringVar()
textVar2 = tkinter.StringVar()

# ---------------------------------- general variables --------------------------------#
done = False # variable for loop connection status
# --------------------------------
iframe = 0
newframe = False

# ------------------------------------- functions ---------------------------#
def getvalues(message_json):
    global iframe, newframe
    try:
        targetCount = message_json["header"]["targetCount"]
        iframe = message_json["header"]["iframe"]

        textVar1.set("Number of detected objects: " + str(targetCount)) # set text and number for gui
        newframe = True # set flag new frame
    except:
        print("Error with parsing information from message")

# --------------------------------       
def connctrl():
    global newframe
    iframeOld = 0
    lasttime = 0
    while done == False:
        if iframe == iframeOld and ((time.time()-lasttime) >= 2): #delay 2 sec.
            connStatus = "Not connected"    # set connecting status to not connected
                          
        if (newframe == True):
            connStatus = "Connected"    # set connecting status to connected
            iframeOld = iframe    # save the actual frame number
            lasttime = time.time() #save actual frame time
            newframe = False    # reset flag new frame
    
        textVar2.set(connStatus) #set text variable connection status
       
# ----------------------------------- mqtt-radar funktion ------------------------------------------------#
class mqtt_radar:
    def __init__(self):
        self.client = mqtt.Client()
        self.client.tls_set(ca_certs=ca_certs)
        self.client.tls_insecure_set(True)
        self.client.on_disconnect = self.on_disconnect
        self.client.on_connect = self.on_connect
        self.client.on_message = self.on_message
        self.client.connect(brokerIp, brokerPort, 60)
        
    def on_message(self, client, serdata, msg):  #called whenever a new message of the subscribed topic recieved
        getvalues(json.loads(msg.payload)) #saving the recived payload in variables
        
    def on_connect(self, client, userdata, flags, rc):
        print("Connected: flags "+str(flags), "Result code "+str(rc))  # gives connection status
        self.client.subscribe(subscribeTopic)
        
    def on_disconnect(self, client, userdata, flags, rc=0):
        print("Disconnected: flags "+str(flags), "Result code "+str(rc)) # gives disconnection status
    
    def start(self):
        self.client.loop_start()
        
    def stop(self):
        self.client.disconnect()
        self.client.loop_stop()
# --------------------------------

# --------------------------------- call mqtt -------------------------------#
mqtt_rd = mqtt_radar()
mqtt_rd.start()
#--------------------------- call connection control ------------------------#
threading.Thread(target=connctrl, daemon=True).start()
# ------------------------------------- gui ---------------------------------#
tkinter.Label(root, textvariable=textVar1, font="Verdana 20", fg='#505050', bg="yellow").pack(expand=1, fill="both")		#, height=2, width=60
tkinter.Label(root, textvariable=textVar2, bg="lightblue").pack(side="left")
tkinter.Button(root, text="Exit", command=root.destroy).pack(side="right")
root.mainloop()

# --------------------------------
done = True	#stop connection control
mqtt_rd.stop()  # dicconnect and stop mqtt



