import os

from launch import LaunchDescription
from launch.actions import (
    DeclareLaunchArgument,
    IncludeLaunchDescription,
)
from launch.conditions import IfCondition
from launch.substitutions import (
    Command,
    LaunchConfiguration,
    PathJoinSubstitution,
)
from launch_ros.actions import Node
from launch_ros.substitutions import FindPackageShare


def generate_launch_description():

    urdf_path = PathJoinSubstitution(
        [FindPackageShare("fulmen_description"),"urdf/","assembly_gazebo.urdf.xacro",]
    )
    rviz_config_path = PathJoinSubstitution(
        [FindPackageShare("fulmen_bringup"),"config/","basic_config.rviz",]
    )
    gazebo_config_path = PathJoinSubstitution(
        [FindPackageShare("fulmen_bringup"),"config/","gazebo_bridge.yaml",]
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                name="urdf", default_value=urdf_path, description="URDF path"
            ),
            DeclareLaunchArgument(
                name="rviz",
                default_value="true",
                description="Run rviz"
            ),
            DeclareLaunchArgument(
                name="use_sim_time",
                default_value="true",
                description="Use simulation time",
            ),

            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                output="screen",
                parameters=[
                    {
                        "use_sim_time": LaunchConfiguration("use_sim_time"),
                        "robot_description": Command(
                            ["xacro ", LaunchConfiguration("urdf")]
                        ),
                    }
                ],
            ),
            IncludeLaunchDescription(
                PathJoinSubstitution([FindPackageShare("ros_gz_sim"),"launch","gz_sim.launch.py",]),
                launch_arguments={
                    "gz_args": [" -r ", "empty.sdf"]
                }.items(),
            ),
            Node(
                package="ros_gz_sim",
                executable="create",
                output="screen",
                arguments=[
                    "-topic",
                    "robot_description",
                    "-entity",
                    "fulmen_robot",
                ],
            ),
            Node(
                package='ros_gz_bridge',
                executable='parameter_bridge',
                name='parameter_bridge',
                parameters=[{
                    'config_file': gazebo_config_path
                }],
                output='screen'
            ),
            Node(
                package="controller_manager",
                executable="spawner",
                arguments=["joint_state_broadcaster"],
            ),
            Node(
                package="controller_manager",
                executable="spawner",
                arguments=["diff_drive_controller"],
            ),
            Node(
                package="rviz2",
                executable="rviz2",
                name="rviz2",
                output="screen",
                condition=IfCondition(LaunchConfiguration("rviz")),
                parameters=[{"use_sim_time": LaunchConfiguration("use_sim_time")}],
                arguments=["-d", rviz_config_path],
            ),
        ]
    )
