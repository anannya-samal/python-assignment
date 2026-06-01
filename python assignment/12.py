from line_follower_robot.sensor import get_sensor_input
from line_follower_robot.movement import decide_movement
user_input = input("Enter 6 sensor values (e.g., 001100): ")

sensor_values, active_sensors = get_sensor_input(user_input)

robot_action = decide_movement(sensor_values)

print("\nExpected Output")
print(f"Sensor Values: {sensor_values}")
print(f"Active Sensors: {active_sensors}")
print(f"Robot Action: {robot_action}")