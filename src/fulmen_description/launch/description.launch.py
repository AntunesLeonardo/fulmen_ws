import os

from launch import LaunchDescription
from launch.actions import DeclareLaunchArgument
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
        [FindPackageShare("fulmen_description"),"urdf/","assembly.urdf.xacro",]
    )

    return LaunchDescription(
        [
            DeclareLaunchArgument(
                name="urdf", default_value=urdf_path, description="URDF path"
            ),
            DeclareLaunchArgument(
                name="rviz",
                default_value="false",
                description="Run rviz"
            ),
            DeclareLaunchArgument(
                name="simulation",
                default_value="false",
                description="Use simulation time",
            ),

            Node(
                package="robot_state_publisher",
                executable="robot_state_publisher",
                name="robot_state_publisher",
                output="screen",
                parameters=[
                    {
                        "use_sim_time": LaunchConfiguration("simulation"),
                        "robot_description": Command(
                            ["xacro ", LaunchConfiguration("urdf")]
                        ),
                    }
                ],
            ),
            Node(
                package="joint_state_publisher",
                executable="joint_state_publisher",
                name="joint_state_publisher",
                parameters=[{"use_sim_time": LaunchConfiguration("simulation")}],
            ),
            Node(
                package="rviz2",
                executable="rviz2",
                name="rviz2",
                output="screen",
                condition=IfCondition(LaunchConfiguration("rviz")),
                parameters=[{"use_sim_time": LaunchConfiguration("simulation")}],
            ),
        ]
    )
