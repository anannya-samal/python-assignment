def process_joint_angles():
    raw_angles = [30,-15, 45, 200, 60, 90]
    
    def get_valid_angles(angles):
        return list(filter(lambda x: 0 <= x <= 180, angles))
    
    def convert_to_servo(angles):
        return list(map(lambda x: x * 10, angles))
    
    valid_angles = get_valid_angles(raw_angles)
    servo_commands = convert_to_servo(valid_angles)
    
    print(f"Valid Angles: {valid_angles}")
    print(f"Servo Commands: {servo_commands}")

process_joint_angles()