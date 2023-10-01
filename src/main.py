import interface
from enum import Enum
import threading
import time

class FSMState(Enum):
    INITIALIZE = 1
    FLIGHT_LOOP = 2
    EXIT = 3

def fsm():
    global state

    if state == FSMState.INITIALIZE:
        print("Hi")
        time.sleep(1)
    

def setup():
    global state

    # setup interface to peripheral devices
    x1 = threading.Thread(target=interface.teraranger_setup, args=("/dev/ttyACM0",))
    #x2 = threading.Thread(target=interface.telemetry_setup, args=("/dev/ttyUSB0",))
    #x3 = threading.Thread(target=interface.depth_sensing_setup)

    # start collecting data
    x1.start()
    x2.start()
    x3.start()

    #put FSM in initial state
    state = FSMState.INITIALIZE



if __name__ == "__main__":
    setup()
    while(True):
        fsm()