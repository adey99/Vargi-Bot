# Vargi-Bot
Inventory Management Bot for eYRC 2020-21, IIT Bombay
#
It is predicted in a study that by 2025, 100 billion connections - 90% from intelligent sensors to machines of all kinds will link the globe as a direct result of information and communication technologies. Industry 4.0 is all about technology intensifying processes involved in manufacturing and warehouse operations. Such as automation in loading and unloading, pick, place and stock management. However, this doesn’t only mean building models for all essential tasks to reduce manual labour but means using automation to smartly work the tasks and make continuous improvements. Almost all warehouse management systems (WMS) follow various inventory practices to optimize processes.

Inspired by this visualisation of Industry 4.0, the current edition of the e-Yantra Robotics Competition features a theme called ‘Vargi-Bots’. Vargi is taken from a Sanskrit word, Vargikaran (वर्गीकरण) which means to separate objects based on their category. The theme is set in the abstraction of a warehouse management system designed in Gazebo, which is a 3D dynamic simulator used to efficiently simulate robots in complex environments.

The arena is an automated warehouse setting where essential packages are required to be sent out to different parts of a city. Since Industry 4.0 heavily focuses on automation here the warehouse will only consist of two industrial robotic arms which will be used by the teams. As the requirements are sent to the warehouse, one robotic arm will identify the packages from a shelf and place them on a conveyor belt and the other robotic arm at the end of the conveyor belt will pick these objects from the conveyor and place them into bins. Each bin represents a destination for the package. As the packages are sent out from the warehouse there will also be alerts sent to the user via email notifying them about the package being shipped from the warehouse.

The packages to be delivered have their own priorities. Packages having a higher priority are intended for a natural disaster or a pandemic situation. Other packages with lower priorities are for general purposes. Similar to a conductor in an orchestra, in this theme, the participants have to design their own conductor (controller) for their warehouse to make smart decisions in order to deliver high priority packages as quickly as possible.

# Task0 Output (Turtle Simulation)

![turtlesim](https://github.com/adey99/Vargi-Bot/blob/master/turtle-dist-optimised.gif)

# Task1 Output (MQTT and HTTP communication)

![turtlesim](https://github.com/adey99/Vargi-Bot/blob/master/mqtt-ros-comm.gif)

# Task2 Output (Pick and Place using RViz and Gazebo)

![rviz](https://github.com/adey99/Vargi-Bot/blob/master/pickplace_complete.gif)

# Task3 Output (Pick and Place from Conveyer Belt)

![task3](https://github.com/adey99/Vargi-Bot/blob/master/Task3-Output.gif)

# Task4 Output (Pick and Place on Conveyer Belt from Shelf and Sort)

https://youtu.be/uOB2JS2OqGs

# Task 5 Output (Complete Warehouse Simulation)

https://youtu.be/pyOjif62lCU