from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    remap_topic_name = ("number", "my_number")

    number_publisher_node = Node(       
        package="my_cpp_pkg",
        executable="number_publisher",
        name="my_number_publisher",    
        remappings=[
            remap_topic_name
        ],
        parameters=[
            {"number_to_publish": 4},
            {"publish_frequency": 2.0}
        ]
    )
    number_counter_node = Node(
        package="my_cpp_pkg",
        executable="number_counter",
        name="my_number_counter",
        remappings=[
            remap_topic_name
        ]
    )

    ld.add_action(number_publisher_node)
    ld.add_action(number_counter_node)

    return ld
