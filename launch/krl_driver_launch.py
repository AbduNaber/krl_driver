from ament_index_python.packages import get_package_share_directory
from launch import LaunchDescription
from launch_ros.actions import Node
from launch.actions import DeclareLaunchArgument
from launch.substitutions import LaunchConfiguration

import os


def generate_launch_description():
    ld = LaunchDescription()
    share_dir = get_package_share_directory('krl_driver')
    krl_driver_node = Node(
        package='krl_driver',
        executable='krl_driver',
        name='krl_driver_node',
        output="screen",
        emulate_tty=True,
    )

    ld.add_action(krl_driver_node)
    return ld
