import paho.mqtt.client as mqtt
import json
import time

BROKER = "broker.emqx.io"
TOPIC_REPORTS = "uoc/control/reports"

def send_result():
    # Your research output
    data = {
        "file": "test3.py",
        "output": "Hello World 3 file",
        "time": time.ctime()
    }
    
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    client.connect(BROKER, 1883, 60)
    client.publish(TOPIC_REPORTS, json.dumps(data))
    client.disconnect()
    print("Report sent!")

if __name__ == "__main__":
    send_result()