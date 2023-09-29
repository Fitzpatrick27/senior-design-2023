import serial

# Configure serial port settings
serial_port = "COM10"  # Replace with the appropriate COM port
baud_rate = 57600  # Replace with the baud rate matching the receiver's configuration

# File path to the PNG file you want to send
png_file_path = "testImage.PNG"

# Define the packet size (in bytes)
packet_size = 16  # You can adjust this as needed

try:
    # Initialize the serial connection
    ser = serial.Serial(serial_port, baud_rate)

    # Open the PNG file for reading
    with open(png_file_path, "rb") as png_file:
        while True:
            # Read a packet of data from the file
            packet = png_file.read(packet_size)
            
            # If no more data is left to send, break the loop
            if not packet:
                break

            # Send the packet over the serial connection
            ser.write(packet)

    print(f"PNG file '{png_file_path}' sent successfully in packets.")
except Exception as e:
    print(f"An error occurred while sending the file: {str(e)}")
finally:
    # Close the serial connection
    if ser.is_open:
        ser.close()
