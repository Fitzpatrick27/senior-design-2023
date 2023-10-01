import serial

def read_from_serial(serial_port):
    try:
        ser = serial.Serial(serial_port, baudrate=57600, timeout=1)
        print("Waiting for data...")
        while True:
            #rawbytes = ser.readline()
            #print(f"received: {rawbytes}")
            line = ser.readline().decode('utf-8').strip()
            if line:
                print(f'Received: {line}')
    except KeyboardInterrupt:
        ser.close()
        print('\nSerial communication stopped.')
    except Exception as e:
        print(f'Error: {e}')
        if ser.is_open:
            ser.close()

# Define the serial port (may vary depending on your system)
serial_port = '/dev/ttyUSB0'

# Read data from the serial port
read_from_serial(serial_port)
