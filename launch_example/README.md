# launch_example
this is launch exanple to launch turtlesim and so on.

[kame](https://github.com/motii8128/launch_example/assets/108280115/824a9873-7b4f-4b1e-8c47-81f65bacfa73)

## environment
|OS|ROS2|safe_drive|
|----|----|----|
|ubuntu22.04|humble|0.2|

You need [turtle_test](https://github.com/motii8128/turtle_test) to use this repository.

## How to use
#### make workspace
```
mkdir ros2_ws/src
cd ros2_ws/src
```

#### clone code
launch_example
```
git clone https://github.com/motii8128/launch_example.git
```
turtle_test
```
git clone https://github.com/motii8128/turtle_test.git
```

#### Build
```
cd ros2_ws
colcon build --cargo-args
```

####  Run
```
ros2 launch launch_example launch.py
```

