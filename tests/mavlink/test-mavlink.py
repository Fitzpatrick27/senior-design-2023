from pymavlink import mavutil

# Connect to Pixhawk
connection = mavutil.mavlink_connection('/dev/serial0', baud=57600)

connection.wait_heartbeat()
print("Heartbeat detected")

command = connection.mav.command_long_encode(
    connection.target_system, connection.target_component,
    mavutil.mavlink.MAV_CMD_DO_SET_MODE, 0,
    0,  # set mode by custom mode (could also use MAV_MODE_FLAG)
    4,  # mode = stabilized
    0, 0, 0, 0, 0)

# Send the command
connection.mav.send(command)

# Wait for a response
response = None
while response is None:
    response = connection.recv_msg()
    if response is not None:
        print(f"Received response: {response}")

connection.close()
