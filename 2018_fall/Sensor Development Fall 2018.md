

# Sensor Development, Fall 2018
#### Dana Owens, Lawrence Li, Lois Lee
#### September 25, 2018

## Abstract

The objective of the Sensor Development subteam is to develop sensors to monitor water quality during the water treatment process. In previous semesters, the subteam developed a working prototype for an in-lab fluidized bed solids detector and also made considerable progress towards prototyping a submersible sludge blanket detector. This semester the subteam will work on finalizing a product-level version of the in-lab fluidized bed solids detector with a more intuitive user interface.The subteam will also work on finishing and determining the best prototype for the sludge blanket detector.


## Introduction

The Sensor Development team aims to create sensors that monitor and report water quality. These sensors can be used in many different steps of the water treatment process. Specifically, these sensors can be used to measure the efficiency of the treatment process and help catch problems if they arise. Originally, in Spring 2017, the Sensor Development subteam worked on developing a gas measurement sensor that would help subteams such as the Anaerobic Fluidized Bed (AFB) Reactor and Upflow Anaerobic Sludge Blanket (UASB) wastewater subteams with their research. 

The following semester, the subteam worked on a fluidized bed solids concentration sensor in order to measure the clay particle concentration in the high rate sedimentation portion of the water treatment process. Over the course of the Fall 2017 and Spring 2018 semesters, the subteam has concentrated on redefining the fluidized bed solids concentration sensor and building a submersible solids concentration sensor to measure turbidity. 

In the Fall 2018 semester, the team hopes to redesign the in-lab fluidized bed solids detector and make it more user-friendly by creating a user interface. The subteam is also currently developing a design for the finalized in-lab fluidized bed solids detector using 3D printing and embedded circuitry that will make the sensor both easier and safer to use. The goal of this sensor to provide the HRS team with a fast method of testing the concentration of clay particles within their testing parameters.  In addition, the subteam is looking into submersibility design options for the turbidity sensor. The goal of the subteam is to finish prototyping the MIA and the MAPE turbidity sensors, which are two design ideas the subteam developed for the submersible sensor the previous semester. The ultimate goal for this sensor is mainly to provide the treatment plant operators with a way to determine the height of the sludge blanket in a way that is both cost-efficient and easy to use. This is especially necessary because it is currently impossible for the plant operators to have a real-time measurement of what occurs within the flocc hopper. This could help determine when the sludge blanket levels are rising. The sensors should help provide insight and information as to what is happening in the plants.

## Previous Work

Discuss what is already known about your research area based on both external work and that of past AguaClara Teams. Connect your objectives with what is already known and explain what additional contribution you intend to make. Make sure to add APA formatted in-text citations. If you mention the author(s) in your sentence, you can simply give the year of publication.[(Logan et. al. 1987)](http://www.jstor.org/stable/pdf/25043431.pdf?acceptTC=true)

Last semester, the sensor development subteam worked on developing the mobile application-processed endoscope (MAPE) turbidity sensor, which could be lowered into sedimentation tanks to measure the distance to the sludge blanket. The sensor utilizes an endoscope to take live images of the water, which are collected and processed for average light intensity by the mobile application component. This sensor enables the calculation of the fluid turbidity from each image. This calculation uses an empirically obtained correlation between turbidity and the intensity of reflected light, as well as offset for any light detected during calibration in clear fluid. The goal of this sensor is to readily measure water turbidity and determine the height of the sludge blanket in a sedimentation tank.

Additionally, the subteam worked on the microcontroller-interfaced analog (MIA) sensor, which houses an analog photodiode, a LED light source, and a microcontroller within a portable casing. Similar to the MAPE turbidity sensor, the MIA sensor measures the fluid turbidity using light intensity. However, this sensor detects light passing through the fluid using a photodiode, which is more reliable and less susceptible to noise. The microcontroller reads the data from the photosensor and converts it into turbidity values, using a relation established through calibration testing. This sensor serves as a prototype for a larger device that will function similarly to the MAPE turbidity sensor, providing treatment plant operators with affordable and user-friendly methods of determining fluid turbidity and the height of the sludge blanket. 

## Fabrication Details


### Fabrication for the Fluidized Beds Solids Detector
The main fabrication for the Fluidized Beds Solids Detector is creating a hard shell that allows the sensor to be more user friendly. The hard shell is made using the software OnShape to create a 3D model of the casing that is eventually printed in a 3D printer. The model is designed by creating a hollow circular base with an inner radius of 0.875 inches and an outer radius of 1.0 inch. Then the base is extruded 6.5 inches and cut in half using a plane that runs parallel to the sensor. These dimension of the diameter of the sensor was designed to create a tight fit for the 1-inch PVC pipe, while also leaving enough room for a layer of foam to house the electronics. The 1-inch PVC pipe was used because the sensor is meant to fit around the HRS team’s apparatus which uses the 1-inch PVC pipe.  The length was an optimization in order to minimize exposure to outside light while allowing for a good fit on the HRS team’s apparatus. To fit properly between the casing and the pipe, the foam should be 2.48 inches wide, 0.18 inches deep and 6.25 inches long. Both the LED and the photosensor are embedded within the foam opposing each other in the center of each side of the sensor.

Figure 1: The model created using the software OnShape. Two copies of this model are 3D printed in order to create a complete casing that will surround the pipe that the sensor will be used on.

After the casing is printed, a layer of foam is epoxied to the inner wall of each side of the casing. The edges of the foam are cut with an X-Acto knife to make sure the foam fits flush with the outer casing and aligns parallel with the edge where the two pieces of the casing come together. Magnetic tape is glued along the length of the casing on the thin, flat surfaces where the two parts of the casing attach together. The magnetic tape is aligned so that when the two shells are attached, they form a cylinder with flush outer walls. In testing, the magnets have been strong enough to hold the two parts of the casing together and create a secure clasp for the sensor.
Cutouts are made in the middle of each piece of foam to fit an LED on one side and a photosensor on the other. The LED and the photosensor are glued to the foam and wires (ground, power, signal) are soldered to these components, looping behind the foam layer and coming out on the bottom of the cylindrical casing, where they are soldered to headers that external cables can plug into, allowing the photosensor and the LED to connect to ProCoDa. The ground, power, and signal wires are marked and color-coded on the outside of the bottom of the casing so the user will know how to connect external wires properly. 

## Special Components
Fluidized Beds Solids Detector 
The photosensor used is the TEMT6000 Ambient Light Sensor made by SparkFun. TEMT6000 is a silicon NPN epitaxial planar phototransistor in a miniature transparent mold for surface mounting onto a printed circuit board. The device is sensitive to wavelengths from 390 nm to 700 nm. It is available here https://www.sparkfun.com/products/8688. 

The LED used … (Include LED info.. We need to find out what LED monroe used)


## Experimental Methods

Set-up
Step 1.

Put tasks in a sequential order.
It is okay to have sub-lists.
Like this.
Experiment
Step 1.

Cleaning Procedure
Step 1.

Current Experimental Methods
Because the team is currently in the fabrication process, the sensor is yet to be tested.

Future Experimental Methods
To develop a voltage-concentration relation for the fluidized bed solids detector, the subteam will attach it to the High Rate Sedimentation recirculator (straight PVC pipe) and experiment with fluids of known solids concentration and turbidity. The photosensor will output a voltage reading based on the amount of light absorbed. This recorded voltage output data will be analyzed and compared to the known concentrations of the fluids to produce a relation between concentration and absorbance, and thus concentration and voltage. 
The subteam will use this calculated voltage-concentration relation to test the sensor on fluids of different known concentrations and record the calculated concentrations from the sensor. As a result, the team can test the accuracy of the photosensor and our relation formulas by comparing the measured concentration/turbidity data to the actual concentrations of the fluids. It may also be necessary to test the effects of different types, particularly different colors, of sediment on the turbidity readings. However, the team is not yet at the testing phase and have no experimentation details yet to report.
