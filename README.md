# Fulmen Project

Fulmen is supposed to be a begginer friendly ROS2 project, to guide on how to begin a mobile, differential drive, robot.

## To do: general

- [x] Update packages setups, descriptions and dependencies.

### To do: simulation on Gazebo

- [x] Robot description;
  - [x] Basic elements
  - [x] Control elements (ros2_control);
  - [x] Control elements gazebo (ros2_control);
  - [x] Description launcher - visualizer.
- [x] Robot bringup gazebo;
  - [x] Bringup file;
  - [x] Gazebo bridge config;
- [ ] Mapping and navigation;
  - [ ] Set up slam_toolbox;
  - [ ] Set up nav2 plugins;
  - [ ] Launcher (either dedicated or within bringup).

### Todo: phisical robot

- [ ] Select harware;
  - [ ] Motors;
  - [ ] Encoders;
  - [ ] Wheels (or tracks);
  - [ ] LiDAR;
  - [ ] Chassis;
  - [ ] Power source and other electrical devices.
- [x] Robot description;
  - [x] Basic elements
  - [x] Control elements (ros2_control);
  - [x] Control elements gazebo (ros2_control);
  - [x] Description launcher - visualizer.
- [ ] Robot bringup;
  - [x] Bringup file - adapt from gazebo bringup;
- [ ] Robot controller (ros2_control);
  - [ ] Hardware driver;
  - [ ] Hardware interface;
  - [ ] Controller.
- [ ] Mapping and navigation;
  - [ ] Set up slam_toolbox;
  - [ ] Set up nav2 plugins;
  - [ ] Launcher (either dedicated or within bringup).
