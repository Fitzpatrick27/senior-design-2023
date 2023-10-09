import serial
import time

def send_string_to_serial(string, serial_port):
    try:
        ser = serial.Serial(serial_port, baudrate=57600, timeout=1)
        ser.write(string.encode())
        ser.close()
        print(f'Successfully sent "{string}" to {serial_port}')
    except Exception as e:
        print(f'Error: {e}')

# Define the string you want to send
string_to_send = "Hewwo! こんにちは あんたばか？？"

# Define the serial port (may vary depending on your system)
serial_port = '/dev/ttyUSB0'

# Send the string
while(True):
    send_string_to_serial(string_to_send, serial_port)
    time.sleep(1.2)

