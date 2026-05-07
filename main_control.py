import paho.mqtt.client as mqtt
import subprocess
import sys
import os
from mcp.server.fastmcp import FastMCP

# Initialize MCP
mcp = FastMCP("mqtt_cloud")

# Your exact topics
TOPIC_COMMANDS = "uoc/research/control"
BROKER = "broker.emqx.io"

@mcp.tool()
def publish_command(command: str) -> str:
    """Publishes a command to uoc/research/control. Use command1, command2, etc."""
    try:
        client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
        client.connect(BROKER, 1883, 60)
        client.publish(TOPIC_COMMANDS, command)
        client.disconnect()
        return f"Successfully sent '{command}' to the system."
    except Exception as e:
        return f"Error: {str(e)}"

# This part runs on your laptop to catch the MQTT message and run the file
def on_message(client, userdata, message):
    cmd = str(message.payload.decode("utf-8")).strip().lower()
    print(f"Received from MQTT: {cmd}")

    py_env = sys.executable
    # Absolute path to your files
    base_dir = "D:/MCP/MQTT_Testing/"
    
    if cmd == "command1":
        subprocess.Popen([py_env, os.path.join(base_dir, "test1.py")])
    elif cmd == "command2":
        subprocess.Popen([py_env, os.path.join(base_dir, "test2.py")])
    elif cmd == "command3":
        subprocess.Popen([py_env, os.path.join(base_dir, "test3.py")])

def start_mqtt():
    mqtt_client = mqtt.Client(callback_api_version=mqtt.CallbackAPIVersion.VERSION2)
    mqtt_client.on_message = on_message
    mqtt_client.connect(BROKER, 1883, 60)
    mqtt_client.subscribe(TOPIC_COMMANDS)
    mqtt_client.loop_start()

if __name__ == "__main__":
    start_mqtt()
    mcp.run()