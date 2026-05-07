import paho.mqtt.client as mqtt
import json

def report():
    client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    client.connect("broker.emqx.io", 1883, 60)
    # The output you requested
    result = {"status": "Success", "data": "Hello World 1 file"}
    client.publish("uoc/control/reports", json.dumps(result))
    client.disconnect()

if __name__ == "__main__":
    print("Running test1.py...")
    report()