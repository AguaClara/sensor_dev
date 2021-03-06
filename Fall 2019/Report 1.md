#### Sonu Kapoor, Saul Bernaber, Rishik Zaparde
 #### Oct 4, 2019

 ## Abstract
 Sensor Development's goal is to develop affordable sensors with readily available materials to monitor and report water quality in the water treatment processes in AguaClara plants and labs. In Fall 2019, the subteam worked on two different projects that were slight modifications from the previous semester. The subteam worked on a second prototype of a Sludge Blanket Detector(SBD) for the upcoming Honduras trip. Additionally, the subteam also started designing a low-cost turbidimeter that would measure the amount of dissolved organics as well as turbidity.

 ## Introduction

 The Sensor Development subteam creates sensors that monitor and report water quality during the water treatment process in AguaClara plants. While turbidimeters exist in the market, they cost upwards of $2000 USD and are often complicated to use. This subteam strives to create affordable and user-friendly sensors with readily available and replaceable parts. The goal is to streamline the measurement process, ensuring that it is not only user-friendly but also accurate. These sensors quantify the effectiveness of the treatment process by measuring the turbidity of the water at different stages of the treatment process.

 The subteam started a second prototype of the submersible Microcontroller-Interfaced Analog (MIA) sensor, which determines when the sludge blanket levels are rising. The ultimate goal for this sensor was to provide the plant operators with a cost-efficient and simple way to determine the height of the sludge blanket inside the floc hopper. This is critical to keep track of the rate at which the sludge blanket is rising. The subteam also started working on a prototype of the low cost turbidity meter for dissolved organics. This project has two main parts - the infrared turbidity meter and the 450nm sensor. This project has been modified from last semester, where the plan was to use an ultraviolet 254nm light sensor. Switching to the 450nm light made this project more economical, as the apparatus required for the UV light sources is more expensive. The turbidimeter is different from the team’s past projects, as it would measure both reflectance and absorbance of the light passing through the water sample. The subteam used an infrared LED and measure the light received directly across and at 90° from the light source. This resulted in a more accurate analysis of water purity, as it accounted for the absorbance of light. The primary use of this sensor will be to measure the amount of dissolved organics in the water - simply measuring turbidity wouldn’t suffice as dissolved organic matter is not always visible.

 ## Previous Work

 In the Spring 2019 semester, the subteam continued work on the three projects from Fall 2018 - the Fluidized Bed Solids Detector (FBSD), the Mobile Application-Processed Endoscope (MAPE), and the Microcontroller-Interfaced Analog (MIA). The team tested the FBSD that was prototyped in Fall 2018 using 3D printing and embedded circuitry. The goal of this sensor was to provide the High Rate Sedimentation (HRS) team with a quick method of testing the concentration of clay particles within their testing parameters. Additionally, the subteam looked into submersibility design options for the turbidity sensor and ways to waterproof the sensor without compromising on accuracy.

 The team also developed a mobile application for the MAPE turbidity sensor. The MAPE turbidity sensor connects an endoscope to an Android smartphone and displays the live feed from the endoscope camera, using the light intensity from the images collected to determine the water turbidity.

 Additionally, the subteam also finished the first prototype of the MIA sensor, which determines when the sludge blanket levels are rising. This sensor housed an analog photodiode (a semiconductor that converts light to electrical current), an LED light source, and a microcontroller inside a portable case. Similar to the MAPE turbidity sensor, the MIA sensor measured the fluid turbidity using light intensity. However, this sensor detected light passing through the fluid using a photodiode, which is more reliable and less susceptible to noise. The microcontroller reads the data from the photosensor and converts it into turbidity values using a relation established through calibration testing. This sensor served as a prototype for a larger device that would function similarly to the MAPE turbidity sensor, providing treatment plant operators with affordable and user-friendly methods of determining fluid turbidity and sludge blanket height. The ultimate goal for the MAPE and MIA sensors was to provide the treatment plant operators with a cost-efficient and simple way to determine the height of the sludge blanket inside the floc hopper. This is critical to keep track of the rate at which the sludge blanket is rising.

A new project was also started that semester, with a goal to build a low-cost turbidimeter with two main parts - the infrared turbidimeter and the 254 nm ultraviolet sensor. The infrared turbidimeter would measure both reflectance and absorbance of the light passing through the water sample by placing two sensors directly across and at 90° from the light source. Accounts for the absorbance of light would result in a more accurate analysis of water purity. The team began testing numerous infrared sources and sensors. In addition, the usefulness of the 254 nm light was researched - this wavelength can be used to measure the amount of organic matter in the water, as organic matter absorbs 254 nm wavelength light.

In Fall 2019, the MAPE app was revisited due to problems surrounding controlling the aperture and exposure of the endoscope, which was interfering with turbidity readings. After looking through the UVCCamera library, it was determined that the MAPE app could no longer be pursued as a viable option. It appears that the code regulating the endoscope's aperture and exposure is embedded in the endoscope itself, which would mean that an external application (i.e. the MAPE app) would not be able to create consistent lighting conditions for turbidity readings.

 ## Fabrication Details

 ### Fabrication Details for the Sludge Blanket Detector

 The Sensor Development team has begun work on fabricating the Sludge Blanket Detector. The original design was theorized to have a few problems and so a few things were modified. The outer surface area was changed to be completely covered in its surroundings so that less light would reach the sensor. More specifically, in the original design, the sensor was surrounded by a clear case all around. This allowed for outside light to affect the readings of turbidity by the sensor. The modifications will allow for the light absorb to be purely coming from the LED and not from reflected or refracted light from the surface. Another change is moving away from using cuvettes to seal the sensor and LED. Instead, PVC will be used in combination with PVC cement. Figure 1 shows a schematic of the old plans for the sensor. (Reference relative dimensions? - SB)

 ![](submersible_model.jpg)
 **Figure 1:** Original Design: Shows the schematic for the MIA sensor. The red wires represent wires to the power source, the black to ground, and the blue to the signal.

 ## Special Components

 ### Special Components for the  Sludge Blanket Detector

 - The photosensor used was the TEMT6000 Ambient Light Sensor from developer SparkFun. TEMT6000 is a silicon NPN epitaxial planar phototransistor in a miniature transparent mold for surface mounting onto a printed circuit board. The device is sensitive to wavelengths from 390 nm to 700 nm. Even as we changed from 254 nm light to 450 nm, the photosensor can still be utilized. It is available [here](https://www.sparkfun.com/products/8688).

 - Because the code relies on the rate of change of light readings rather than the absolute value of light intensity, the LED used in this sensor is irrelevant and open to change. In the Spring 2019 iteration, the LED used was a small white LED running on 3V, however any LED such as those from [here](www.sparkfun.com) would work well.

 ### Special Components for the Low-Cost Turbidimeter

- The Arduino Mega 2560 was bought from the distributor Digi-Key. Its part number is [1050-1018-ND](https://www.digikey.com/products/en?keywords=1050-1018-ND).
- The SD card module that works with the arduino was also bought from Digi-Key. Its part number is [1528-1462-ND](https://www.digikey.com/products/en?WT.z_se_ps=1&keywords=1528-1462-ND).
- The laser diode used is of infrared type with wavelength 850nm. Six models of the lasers were bought from the distributor Digi-Key. These are the part numbers: [365-1877-ND](https://www.digikey.com/products/en?keywords=365-1877-ND), [365-1878-ND](https://www.digikey.com/products/en?keywords=365-1878-ND), [365-1879-ND](https://www.digikey.com/products/en?keywords=365-1879-ND), [365-1880-ND](https://www.digikey.com/products/en?keywords=365-1880-ND), [365-1881-ND](https://www.digikey.com/products/en?keywords=365-1881-ND), and [365-1883-ND](https://www.digikey.com/products/en?keywords=365-1883-ND).
- Along with the laser diodes, five infrared sensors were also tested. These are most sensitive at 850nm wavelength. These were bought from [T.T. Electronics](https://www.ttelectronics.com/). The following table has relevant information regarding these sensors.
- Refer to table 1 for datasheets and links to the sensors mentioned above.

**Table 1. Details for sensors.**

Part number | Description | Datasheet Link
------------ | ------------- | -------------
OP830SL | Phototransistor, Photodarlington, NPN Silicon, TO-18 Dome Lens | [Datasheet](https://www.ttelectronics.com/TTElectronics/media/ProductFiles/Optoelectronics/Datasheets/OP800_830_SLandWSL.pdf)
OP804SL | Op804Sl IR Phototransistor, Through hole 3-pin TO-18 Package | [Datasheet](https://www.ttelectronics.com/TTElectronics/media/ProductFiles/Optoelectronics/Datasheets/OP800_830_SLandWSL.pdf)
OP805SL | Sensor, Opto switch assemble, transmissive, single channel; 5.1mm; 30V; 50mA | [Datasheet](https://www.ttelectronics.com/TTElectronics/media/ProductFiles/Optoelectronics/Datasheets/OP800_830_SLandWSL.pdf)
OP913WSL | Sensor, Opto switch assemble, transmissive, single channel; 3.8mm; 30V; 20mA | [Datasheet](https://www.ttelectronics.com/TTElectronics/media/ProductFiles/Optoelectronics/Datasheets/OP913.pdf)
OP812SL-OC | Photologic TO-18 | [Datasheet](https://www.ttelectronics.com/TTElectronics/media/ProductFiles/Optoelectronics/Datasheets/OPL800.pdf)

## References
Li, L., Lee, L., Vangavolu, S., Kapoor, S. (2018, December). Fall 2018 Manual. Retrieved from:
https://github.com/AguaClara/sensor_dev/blob/master/Spring%202019/SensorDev-Spring-2019-Final-Report.md
