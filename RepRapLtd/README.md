# An open-source 6 degrees-of-freedom input device

[RepRap Ltd](https://reprapltd.com)


## How far have we got?

![Hall force sensor](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Pictures/force-sensor-real-cad.jpg)

Based on our [experiments on our original force-sensor design](https://github.com/RepRapLtd/6DInput/tree/main/RepRapLtd/Experiments/ForceSensor) we have created a new force sensor illustrated above.

The actual device is on the left and the FreeCAD design is on the right. It consists of a printed part with two 1.5 mm x 15 mm brass rods inserted into holes to act as sliders. On the right the magnet is shown green, and the Hall sensor is blue. The curved part at the left end of the sensor is a printed spring. The four holes in the sides allow self-tapping M2 screws to be used to attach the force sensor to whatever is pushing and pulling it. The top left screw is longer than the others as it also retains the brass rods.

The FreeCAD design is [here](https://github.com/RepRapLtd/6DInput/tree/main/RepRapLtd/Mechanics/force-sensor-V1.FCStd).

Once again, the magnets [were these](https://www.amazon.co.uk/gp/product/B00TACH0P2), and the Hall sensors were OH49E s.

This design has the following advantages:

 - It has just one integrated printed part,
 - It gives true parallel motion, with no other movement or twist possible, and
 - The additional components are cheap and easy to obtain anywhere.


## Experiments

![force sensor test](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Experiments/ForceSensor/calibration.jpg)

We used a calibration jig based on our design for our first calibration experiments illustrated above. The FreeCAD file for the latest jig is in [here](https://github.com/RepRapLtd/6DInput/tree/main/RepRapLtd/Mechanics/calibration-jig.FCStd).

Here is the result of loading and unloading the device:

![test graph](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Experiments/ForceSensor/slider-force-voltage-graph.png)

As in our previous experiments, there is a certain amount of hysteresis, as would be expected with a plastic spring. But as you will see this does not impede the performance of the sensor. The red line is the least-squares linear fit, which has the equation shown.

We made two more sensors, giving us three in total. Then we wrote a Python program to read them and to use their output to rotate a cube about the *X, Y* and *Z* axes in 3D on the screen. This worked, and the sensor felt good in use; letting go of the sensors stopped the cube moving; pushing and pulling rotated the cube in all directions; and the harder the push or pull the faster it moved.

There is a video of this working [here](https://github.com/RepRapLtd/6DInput/tree/main/RepRapLtd/Pictures/os3dmouse.mp4) and here is a still from that:

![1D animation](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Pictures/3D-spacemouse-test.jpg)

The Python program is [here](https://github.com/RepRapLtd/6DInput/tree/main/RepRapLtd/Software/3DGraphics/3dmouse.py) and the Arduino program that reads the Hall sensor and talks to the Python program is [here](https://github.com/RepRapLtd/6DInput/tree/main/RepRapLtd/Software/ArduinoHallReader/ArduinoHallReader.ino).

## Update

We realised from the success of this that it would be easy to design a 2D joystick that used the same principles.  This is the result:

![joystick](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Pictures/joystick.jpg)

And here is the FreeCAD design (which is [here](https://github.com/RepRapLtd/6DInput/tree/main/RepRapLtd/Mechanics/2D-joystick-V1.FCStd) in the repository):

![cad joystick](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Pictures/joystick-cad.png)

Once again the magnets are green and the Hall sensors are blue.  The central block has a square spring attaching it to the base (red for clarity, but printed like the other two parts).  The holes are for self-tapping M2 screws to attach each part of the device to a handle or a solid base.

If you make one glue the magnets in (Araldite, not cyanoacrylate) with the same pole facing outwards from the sprung block. This is tricky because the fields pull them the other way round and they tend to flip over. Force them right and clamp them while the glue sets.

The device connected to the Python program without modifying that (though it has now been updated to use numpy vector arithmetic for neatness and brevity). It worked well, allowing the cube to be tumbled on the screen as in the video above.

This joystick may form part of the final open-source 3D mouse, but it may also be useful to people in its own right as it is very easy to print and the cost of the components is very small.

## Update 2

We have now added rotation about Z to that to create a device that does all possible rotations.

![XYZ joystick](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Pictures/XYZ-joystick-photo.jpg)

And here is the FreeCAD design (which is [here](https://github.com/RepRapLtd/6DInput/tree/main/RepRapLtd/Mechanics/XYZ-joystick-V1.FCStd) in the repository):

![XYZ cad joystick](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Pictures/XYZ-joystick-CAD.png)

The two holes in the top are for self-tapping M2 screws to attach the device to a handle. The base will screw into the device that detects X, Y and Z translations. The FreeCAD design is here.

There is a video of the device working [here in the repository](https://github.com/RepRapLtd/6DInput/tree/main/RepRapLtd/Pictures/XYZ-joystick.mp4) 



