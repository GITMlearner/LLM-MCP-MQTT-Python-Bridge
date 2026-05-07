# LLM-MCP-MQTT-Python-Bridge
This repository demonstrates a bidirectional communication system that allows a local Large Language Model (LLM) to orchestrate physical and digital tasks using the Model Context Protocol (MCP) and MQTT


Step 1: The Command (LLM $\rightarrow$ MCP): The user provides a natural language prompt to the local LLM. The LLM identifies the intent and calls the publish_command tool via MCP.Step

2: The Transmission (MCP $\rightarrow$ MQTT): The MCP server publishes a short-code (e.g., "1") to the MQTT broker on the topic uoc/research/control.Step 

3: The Reception (MQTT $\rightarrow$ Python): The main_control.py script, running a background MQTT listener, receives the message and maps the short-code to a local file path.Step 

4: The Execution (Python Subprocess): The controller triggers the specific .py file (e.g., test1.py) using a system subprocess.Step 

5: The Feedback (Python $\rightarrow$ MQTT): The executed script performs its task and independently publishes a JSON result back to the broker on uoc/control/reports.Step

6: Monitoring: The final output appears in the MQTTX dashboard or any subscribed client.
