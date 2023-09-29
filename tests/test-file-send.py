import serial
import time
import shutil

# Serial port settings
serial_port = "COM10"  # Replace with the appropriate COM port
baud_rate = 57600  # Replace with the baud rate of your serial connection

# File paths
local_file_path = "sendTest.txt"  # Replace with the local file path
remote_file_path = "sendTest.txt"  # Replace with the desired remote file path

# Initialize the serial connection


# Wait for a brief moment to ensure the serial connection is established
time.sleep(2)
while(True):
    try:
        ser = serial.Serial(serial_port, baud_rate)
        # Open the local file for reading
        with open(local_file_path, "rb") as local_file:
            # Read the file contents
            file_data = local_file.read()

            # Send the file data over the serial connection
            ser.write(file_data)

            # Wait for a moment to allow the data to be sent
            time.sleep(2)

        # Close the serial connection
        ser.close()

        print(f"File '{local_file_path}' sent to '{serial_port}:{remote_file_path}' successfully.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")
    finally:
        # Ensure the serial connection is closed, even in case of an exception
        if ser.is_open:
            ser.close()
