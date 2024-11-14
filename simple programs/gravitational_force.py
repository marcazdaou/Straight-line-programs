import stdio
import sys

# accepts m1 (float), m2 (float), and r (float) as command-line arguments
m1 = float(sys.argv[1])
m2 = float(sys.argv[2])
r = float(sys.argv[3])
G = 6.674e-11

# writes to standard output the gravitational force f (in N) acting between the objects
f = G * ((m1 * m2) / r**2)

# Compute and write the value of gravitational force f
stdio.writeln(f)
