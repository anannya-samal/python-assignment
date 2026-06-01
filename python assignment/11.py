def decide_movement(sensors):
    
    # Rule 1: If all sensors are 0
    if sensors == [0, 0, 0, 0, 0, 0]:
        return "Stop Robot"
        
    # Rule 2: If all sensors are 1
    elif sensors == [1, 1, 1, 1, 1, 1]:
        return "Junction Detected"
        
    # Rule 3: If middle sensors detect line (index 2 or 3 is a 1)
    elif sensors[2] == 1 or sensors[3] == 1:
        return "Move Forward"
        
    # Rule 4: If left sensors detect line (index 0 or 1 is a 1)
    elif sensors[0] == 1 or sensors[1] == 1:
        return "Turn Left"
        
    # Rule 5: If right sensors detect line (index 4 or 5 is a 1)
    elif sensors[4] == 1 or sensors[5] == 1:
        return "Turn Right"
        
    # Just in case something weird happens, stop the robot
    else:
        return "Stop Robot"