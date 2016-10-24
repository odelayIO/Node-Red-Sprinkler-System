
##### View on [gh-page](https://odelayio.github.io/Node-Red-Sprinkler-System/)


# Node-Red Home Sprinkler System 


## Introduction

I wanted to experiment with Node-Red to develop a web based home sprinkler system.  I choose Node-Red because it.s web based, therefore it could be used using a mobile phone.  I wanted a way to manually control my home sprinkler system and have more control when the lawn is watered.  In addition, I wanted to develop a system that can be expanded in the future (e.g. embed small wireless moisture sensors and have the system report when I need to water the lawn).  

At the moment I just created a Node-Red flow using the node-red-dashboard Node.  I have been using LabVIEW home version for [past projects to provide a GUI](http://odelayio.github.io/panStamp-IoT-Evaluation/).  This project is far from complete, but I.ve only spent several hours of development and was able to prove that Node-Red is a possible solution for this problem.

<br>


## Node-Red 
I recently upgraded to a Raspberry Pi 3 and installed Jessie OS.  Node-Red is pre-installed in the OS.  I did need to install the node-red-dashboard for this project.  Installing Nodes is very straight forward, and very well documented.

- [Running on Raspberry Pi](http://nodered.org/docs/hardware/raspberrypi)

- [node-red-dashboard download]( http://flows.nodered.org/node/node-red-dashboard)


<br>

## Node-Red Flow

This project includes two flows, and they are linked together through a menu.  The two flows have the following features:

#### Flow 1 : Provides a way trigger the sprinkler system to turn on for a configurable set of time.  
![flow1.jpg](http://odelay.io/projects/Sprinkler/flow1.jpg)

#### Flow 2 : Provides a way to manually control the sprinkler system by using a standard ON/OFF switch.
![flow2.jpg](http://odelay.io/projects/Sprinkler/flow1.jpg)

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



