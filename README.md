# Harvtech_joystick
I am using this to check if the joystick is getting read by the IntelNuc and we can furthur work on it.

# Notes for initial installation 

1.Install the necessary ROS packages: Make sure ROS installed on the computer. Additionally, need to install the joystick driver package. Install it using the following command:
  ```
    sudo apt-get install ros-noetic-joy
  ```
  
2. Configure the joystick: Before we can use the joystick, we need to identify the device name associated with it. To determine the device name, the following is the command: 
```
ls /dev/input/
```
3. Then roscore is run. Then on a diff terminal:
```
rosparam set joy_node/dev "/dev/input/jsX"
rosrun joy joy_node
```

# Notes for running the code
1. Copy the above files in the catkinworkspace, src folder.
2. Then outside the folder run `catkin_make` in terminal.
3. Then finally: 
  ```
    rosrun <your_package_name> joy_listener.py
    
  ```
