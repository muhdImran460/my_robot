from launch import LaunchDescription
from launch_ros.actions import Node

def generate_launch_description():
    ld = LaunchDescription()

    remap_topic_name = ("robot_news", "kuah_kandaq_FM")

    robot_FLY_FM = Node(
        package="my_cpp_pkg",
        executable="robot_news_station",
        name="robot_FLY_FM",
        remappings=[
            remap_topic_name
        ],
        parameters=[
            {"robot_name": "K-2S0"},
            {"publish_frequency": 0.5}
        ]
    ) 
    robot_HITZ_FM = Node(
        package="my_cpp_pkg",
        executable="robot_news_station",
        name="robot_HITZ_FM",
        remappings=[
            remap_topic_name
        ],
        parameters=[
            {"robot_name": "BD-1"},
            {"publish_frequency": 0.2}
        ]
    )
    robot_MIX_FM = Node(
        package="my_cpp_pkg",
        executable="robot_news_station",
        name="robot_MIX_FM",
        remappings=[
            remap_topic_name
        ],
        parameters=[
            {"robot_name": "R2D2"},
            {"publish_frequency": 1}
        ]
    )
    robot_MUTIARA_FM = Node(
        package="my_cpp_pkg",
        executable="robot_news_station",
        name="robot_MUTIARA_FM",
        remappings=[
            remap_topic_name
        ],
        parameters=[
            {"robot_name": "BB-8"},
            {"publish_frequency": 1.5}
        ]
    )
    robot_ERA = Node(
        package="my_cpp_pkg",
        executable="robot_news_station",
        name="robot_ERA",
        remappings=[
            remap_topic_name
        ],
        parameters=[
            {"robot_name": "C3P0"},
            {"publish_frequency": 0.8}
        ]
    ) 

    smartphone = Node(
        package="my_cpp_pkg",
        executable="smartphone",
        name="smartphone",
        remappings=[
            remap_topic_name
        ]
    )  

    ld.add_action(robot_FLY_FM)
    ld.add_action(robot_ERA)
    ld.add_action(robot_HITZ_FM)
    ld.add_action(robot_MIX_FM)
    ld.add_action(robot_MUTIARA_FM)
    ld.add_action(smartphone)

    return ld
