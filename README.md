##### View on [gh-page](https://odelayio.github.io/Node-Red-Sprinkler-System/)


# Node-Red Home Sprinkler System 


## Introduction

This is a home sprinkler system using Node-Red hosted on a Raspberry Pi 3 Model B.  Node-Red the language to use to develop applications (web and/or mobile) for the IoT.  I used the Node-Red-Dashboard Node to implement a GUI to control four (4) area home sprinkler system.  At the moment I just have LEDs attached to the Raspberry PI GPIO, but I plan to use a relay board to control the sprinkler valves. 

<br>


## Node-Red 
I recently upgraded to a Raspberry Pi 3 and installed Jessie OS.  Node-Red is pre-installed in the OS.  I did need to install the node-red-dashboard for this project.  Installing Nodes is very straight forward, and very well documented.

- [Running on Raspberry Pi](http://nodered.org/docs/hardware/raspberrypi)

- [node-red-dashboard download]( http://flows.nodered.org/node/node-red-dashboard)


<br>

## Node-Red Flow

This project includes two flows, and they are linked together through a menu.

#### Flow 1 : Provides a way trigger the sprinkler system to turn on for a configurable set of time.  
![flow1.jpg](http://odelay.io/projects/Sprinkler/flow1.jpg)

#### Flow 2 : Provides a way to manually control the sprinkler system by using a standard ON/OFF switch.
![flow2.jpg](http://odelay.io/projects/Sprinkler/flow2.jpg)

<br>


#### Mobile App GUI

![mobileflow1](http://odelay.io/projects/Sprinkler/mobile_flow1.png)

![mobileflow2](http://odelay.io/projects/Sprinkler/mobile_flow2.png)

![mobilemenu](http://odelay.io/projects/Sprinkler/mobile_menu.png)
<br>

#### Webpage (PC) GUI


![web_flow1](http://odelay.io/projects/Sprinkler/web_flow1.jpg)

<br>


#### Raspberry PI LED (Soon to be replaced with Relay Board)

![rpi_led2](http://odelay.io/projects/Sprinkler/rpi_led2.jpg)





