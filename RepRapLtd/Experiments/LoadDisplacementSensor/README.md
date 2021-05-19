# A simple force sensor using the Hall effect

Adrian Bowyer


## The Idea

![Hall force sensor](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Experiments/LoadDisplacementSensor/sensor-real-cad.jpg)

Based on our [experiments in measuring positions in space](https://github.com/RepRapLtd/6DInput/tree/main/RepRapLtd/Experiments/HallCalibration) using Hall sensors we decided to make a simple force sensor.

To start with, we used our previous experimental setup to plot a graph of voltage (in Arduino analogue to digital converter readings; [0, 1023]) against the displacement that generated that voltage:

![voltage vs. distance](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Experiments/LoadDisplacementSensor/voltage-distance-graph.png)

Once again, the magnets [were these](https://www.amazon.co.uk/gp/product/B00TACH0P2), and the Hall sensors were OH49E s. The voltage is the dependent variable, obviously, but we plotted it on the *X* axis because in general you would want to know the displacement given a voltage reading.

Based on this graph we decided to make a system with a 5mm gap between the magnet and the sensor at zero force, with displacements of +/- 1mm for forces of 5N or so.

The picture at the top shows the resulting design for the sensor. On the left is a photograph of it assembled, and on the right is an exploded view of the two printed parts that make it up. It is about 25mm square and 8 mm deep.

You can see the three wires of the Hall sensor (orange in the photograph; blue in the CAD design). The magnet is embedded in the opposite projection. Here is a CAD picture showing it the other way up; the magnet is green:

![magnet in sensor](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Experiments/LoadDisplacementSensor/sensor-other-half-cad.png)

The four thin rectangular sections form the spring. The four small circular holes are mounting holes for self-tapping M2 screws.

The reason we made it in two halves was so that the four spring elements could be printed flat against the printer's bed without support. To assemble it the magnet and the Hall sensor are glued into their respective halves with superglue, and the two halves are then glued together.

The [CAD file is here](https://github.com/RepRapLtd/6DInput/tree/main/RepRapLtd/Mechanics) in the file force-displacement-sensor-V2.FCStd.


## Experiments

![force sensor test](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Experiments/LoadDisplacementSensor/calibration.jpg)

We designed a test jig for the device (it's in the same CAD file) that allows it to be loaded in either direction by hanging weights on two threads running over two pulleys. The Hall voltages were logged by an Arduino, which you can also see.

Here is the resulting force-voltage graph showing a full cycle starting with 700g on the left thread, reducing that to 0g, adding the weights to the right thread, and then reversing that entire sequence:

![test graph](https://github.com/RepRapLtd/6DInput/blob/main/RepRapLtd/Experiments/LoadDisplacementSensor/force-voltage-graph.png)

As the springs are plastic some hysterisis would be expected, and you can see that has occured. The red line and the formula is a best-fit linear approximation to the results.



