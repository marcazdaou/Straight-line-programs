import math
import stdio
import sys

# t accepts θ1 (float), n1 (float), and n2 (float) as command-line arguments
theta1 = float(sys.argv[1])
n1 = float(sys.argv[2])
n2 = float(sys.argv[3])


#  writes to standard output the corresponding angle of refraction θ2 in degrees
theta2 = math.asin((math.sin(math.radians(theta1)) * n1) / n2)

# Compute and write the value of the angle of refraction θ2 in degrees
stdio.writeln(math.degrees(theta2))
