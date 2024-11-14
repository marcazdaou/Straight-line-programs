import math
import stdio
import sys

# A (float) and t (float) as command-line arguments
A = float(sys.argv[1])
t = float(sys.argv[2])

# writes the probability p to standard output.
p = math.exp(-A * t)

#  Compute and write the value of p
stdio.writeln(p)
