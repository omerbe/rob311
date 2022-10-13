import numpy as np
import time

EXEC_TIME = 5
FREQ = 200
DT = 1/FREQ

if __name__ == "__main__":
    start = time.time()
    t = 0.0
    x=0
    last_timestop = 0
    while (time.time() - start) < 5:
        printcheck = time.time() - last_timestop
        if printcheck >= DT:
            last_timestop = time.time()
            print("ROB311 @UM-ROBOTICS")
            x +=1
    print (x)
    # Print "ROB311 @UM-ROBOTICS" for 5 seconds @200Hz

    # YOUR
    # CODE 
    # GOES 
    # HERE
