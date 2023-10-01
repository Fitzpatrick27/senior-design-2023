import serial

def read_from_serial(serial_port):

    ser = serial.Serial(serial_port, baudrate=57600, timeout=1)

    try:
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

def read_file_from_serial(serial_port):

    ser = serial.Serial(serial_port, baudrate=57600, timeout=10)

    # Receive the image size
    image_size = int.from_bytes(ser.read(4), byteorder='big')

    try:
        print("Waiting for data...")

        received_data = b''
        current_packet_count = 0
        while len(received_data) < image_size:
            received_data += ser.read(128)
            current_packet_count += 1
            print("packet count:",current_packet_count)

        with open("received_image.jpeg", 'wb') as file:
            print("saving image...")
            file.write(received_data)
        
        print("File saved as received_image.jpeg")
            
    except KeyboardInterrupt:
        ser.close()
        print('\nSerial communication stopped.')
    except Exception as e:
        print(f'Error: {e}')
        if ser.is_open:
            ser.close()

# Define the serial port (may vary depending on your system)
# Linux
#serial_port = '/dev/ttyUSB0'
# MacOS
serial_port = '/dev/tty.usbserial-D30EZ678'

# Read data from the serial port
#read_from_serial(serial_port)
read_file_from_serial(serial_port)
