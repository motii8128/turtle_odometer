from launch import LaunchDescription , actions
from launch_ros.actions import Node
from ament_index_python.packages import get_package_share_directory
import os.path

def generate_launch_description():
                
        return LaunchDescription([
            # turtlesim
            Node(
                 package='turtlesim',
                 executable='turtlesim_node',
                 on_exit=actions.Shutdown(),
            ),
            # test node
            Node(
                 package='turtle_test',
                 executable='turtle_test',
                 on_exit=actions.Shutdown(),
            ),
        ])