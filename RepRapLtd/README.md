# An open-source 6 degrees-of-freedom input device

[RepRap Ltd](https://reprapltd.com)


## How far have we got?

![Hall force sensor](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Pictures/force-sensor-real-cad.jpg)

Based on our [experiments on our original force-sensor design](https://github.com/RepRapLtd/6DInput/tree/main/RepRapLtd/Experiments/ForceSensor) we have created a new version illustrated above.

The actual device is on the left and the FreeCAD design (in Mechanics/force-sensor-V1.FCStd under this folder) is on the right. It consists of a printed part with two 1.5 mm x 15 mm brass rods inserted into holes to act as sliders. The magnet is shown green, and the Hall sensor is blue. The curved part at the left end is a printed spring. The four holes in the sides allow self-tapping M2 screws to be used to attach the force sensor to whatever is pushing and pulling it. The top left screw is longer than the others as it also retains the brass rods.

Once again, the magnets [were these](https://www.amazon.co.uk/gp/product/B00TACH0P2), and the Hall sensors were OH49E s.

This design has the following advantages:

 - Just one integrated printed part
 - True parallel motion, with no other movement or twist possible
 - Additional parts are cheap and easy to obtain anywhere


## Experiments

![force sensor test](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Experiments/ForceSensor/calibration.jpg)

We used a calibration jig based on our design for our first calibration experiments illustrated above. The FreeCAD file for the latest version is in Mechanics/calibration-jig.FCStd under this folder.

Here is the result of loading and unloading the device:

![test graph](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Experiments/ForceSensor/slider-force-voltage-graph.png)

Again, there is a certain amount of hysteresis, as would be expected with a plastic spring. But as you will see this does not impeed the performance of the sensor.

We then wrote a Python program to read the force sensor and to use its output to rotate a cube in 3D on the screen. This worked, and the sensor felt right in use; letting go of the sensor stopped the cube moving; pushing and pulling rotated it in either direction; and the harder the push the faster it moved.

There is a video of this working in Pictures/1D-spacemouse-test.mp4 and here is a still from that:

![1D animation](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Pictures/1D-spacemouse-test.jpg)

The Python program is in Software/3DGraphics/3dmouse.py and the Arduino program that reads the Hall sensor and talks to the Python program is in Software/CalibrationMapArduino/CalibrationMapArduino.ino .





