import math
import stdio
import sys

# accepts latitude ϕ (float) and longitude λ (float) as command-line argument
latitude = float(sys.argv[1])
longitude = float(sys.argv[2])

# Write the corresponding x and y values to standard output
x = longitude
y = math.log((1 + math.sin(math.radians(latitude))) / (1 - math.sin(math.radians(latitude)))) / 2

#  Compute and write the values of x and y, separated by a space
stdio.write(x)
stdio.write(" ")
stdio.writeln(y)
