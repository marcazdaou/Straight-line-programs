import stdio
import sys

# accepts t (float) and v (float) as command-line arguments
t = float(sys.argv[1])
v = float(sys.argv[2])

#  writes the wind chill w to standard output
w = 35.74 + 0.6215 * t + (0.4275 * t - 35.75) * v ** 0.16

# Compute and write the value of wind chill w
stdio.writeln(w)
