
# Sensor Development, Fall 2018
#### Dana Owens, Lawrence Li, Lois Lee
#### September 25, 2018

## Abstract

The objective of the Sensor Development subteam is to develop sensors to monitor water quality during the water treatment process. In previous semesters, the subteam developed a working prototype for an in-lab fluidized bed solids detector and also made considerable progress towards prototyping a submersible sludge blanket detector. This semester the subteam will work on finalizing a product-level version of the in-lab fluidized bed solids detector with a more intuitive user interface.The subteam will also work on finishing and determining the best prototype for the sludge blanket detector.


## Introduction

The Sensor Development team aims to create sensors that monitor and report water quality. These sensors can be used in many different steps of the water treatment process. Specifically, these sensors can be used to measure the efficiency of the treatment process and help catch problems if they arise. Originally, the Sensor Development subteam worked on developing a gas measurement sensor that would help subteams such as the Anaerobic Fluidized Bed (AFB) Reactor and Upflow Anaerobic Sludge Blanket (UASB) wastewater subteams with their research. 

The following semester, the subteam worked on a fluidized bed solids concentration sensor in order to measure the clay particle concentration in the high rate sedimentation portion of the water treatment process. Over the past year the subteam has concentrated on redefining the fluidized bed solids concentration sensor and building a submersible solids concentration sensor to measure turbidity. 

This semester, the team hopes to redesign the in-lab fluidized bed solids detector and make it more user-friendly by creating a user interface. The subteam is also currently developing a design for the finalized in-lab fluidized bed solids detector using 3D printing and embedded circuitry that will make the sensor both easier and safer to use. The goal of this sensor to provide the HRS team with a fast method of testing the concentration of clay particles within their testing parameters.  In addition, the subteam is looking into submersibility design options for the turbidity sensor. The goal of the subteam is to finish prototyping the MIA and the MAPE turbidity sensors, which are two design ideas the subteam developed for the submersible sensor the previous semester. The ultimate goal for this sensor is mainly to provide the treatment plant operators with a way to determine the height of the sludge blanket in a way that is both cost-efficient and easy to use. The sensors should help provide insight and information as to what is happening in the plants.

## Previous Work

Last semester, the sensor development subteam worked on developing the mobile application-processed endoscope (MAPE) turbidity sensor, which could be lowered into sedimentation tanks to measure the distance to the sludge blanket. The sensor utilizes an endoscope to take live images of the water, which are collected and processed for average light intensity by the mobile application component. This sensor enables the calculation of the fluid turbidity from each image. This calculation uses an empirically obtained correlation between turbidity and the intensity of reflected light, as well as offset for any light detected during calibration in clear fluid. The goal of this sensor is to readily measure water turbidity and determine the height of the sludge blanket in a sedimentation tank.

Additionally, the subteam worked on the microcontroller-interfaced analog (MIA) sensor, which houses an analog photodiode, a LED light source, and a microcontroller within a portable casing. Similar to the MAPE turbidity sensor, the MIA sensor measures the fluid turbidity using light intensity. However, this sensor detects light passing through the fluid using a photodiode, which is more reliable and less susceptible to noise. The microcontroller reads the data from the photosensor and converts it into turbidity values, using a relation established through calibration testing. This sensor serves as a prototype for a larger device that will function similarly to the MAPE turbidity sensor, providing treatment plant operators with affordable and user-friendly methods of determining fluid turbidity and the height of the sludge blanket. 

