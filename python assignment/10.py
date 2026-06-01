def get_sensor_input(input_str):
    
    char_list = list(input_str)
       
    sensor_values = list(map(int, char_list))
     
    def saw_line(value):
        return value == 1
        
    active_ones = list(filter(saw_line, sensor_values))
    
    active_sensors = len(active_ones)
    
    return sensor_values, active_sensors
   